import os
# import openai
from openai import OpenAI
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
import pdfplumber
from docx import Document
import spacy
from textblob import TextBlob
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

nlp = spacy.load('en_core_web_sm')

# Set your OpenAI API key
client = OpenAI(api_key='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')



@app.route('/')
def index():
    return 'Welcome to the Resume Enhancer API!'


@app.route('/test')
def test():
    return jsonify({'message': 'Hello from the backend!'})


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'resume' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['resume']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # Create the upload folder if it doesn't exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        file.save(filepath)
        return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 200
    else:
        return jsonify({'error': 'Invalid file type'}), 400


def parse_pdf(filepath):
    with pdfplumber.open(filepath) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text


def parse_docx(filepath):
    doc = Document(filepath)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)


@app.route('/parse/<filename>', methods=['GET'])
def parse_resume(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.exists(filepath):
        return jsonify({'error': 'File not found'}), 404

    if filename.endswith('.pdf'):
        resume_text = parse_pdf(filepath)
    elif filename.endswith('.docx'):
        resume_text = parse_docx(filepath)
    else:
        return jsonify({'error': 'Unsupported file type'}), 400

    # Implement logic for enhancement/suggestions based on resume_text

    return jsonify({'resume_text': resume_text}), 200


def calculate_readability(text):
    blob = TextBlob(text)
    return blob.sentiment


@app.route('/analyze/<filename>', methods=['GET'])
def analyze_resume(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.exists(filepath):
        return jsonify({'error': 'File not found'}), 404

    if filename.endswith('.pdf'):
        resume_text = parse_pdf(filepath)
    elif filename.endswith('.docx'):
        resume_text = parse_docx(filepath)
    else:
        return jsonify({'error': 'Unsupported file type'}), 400

    doc = nlp(resume_text)

    # Extract entities and keywords
    entities = [{'text': ent.text, 'label': ent.label_} for ent in doc.ents]
    keywords = [token.text for token in doc if not token.is_stop and not token.is_punct]

    # Calculate readability
    sentiment = calculate_readability(resume_text)

    return jsonify({
        'entities': entities,
        'keywords': keywords,
        'sentiment': {
            'polarity': sentiment.polarity,
            'subjectivity': sentiment.subjectivity
        },
        'resume_text': resume_text
    }), 200


@app.route('/jobdescription', methods=['POST'])
def analyze_job_description():
    if 'job_description' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['job_description']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        if filename.endswith('.pdf'):
            job_text = parse_pdf(filepath)
        elif filename.endswith('.docx'):
            job_text = parse_docx(filepath)
        else:
            return jsonify({'error': 'Unsupported file type'}), 400

        doc = nlp(job_text)
        job_keywords = [token.text for token in doc if not token.is_stop and not token.is_punct]
        return jsonify({'job_keywords': job_keywords, 'job_text': job_text}), 200
    return jsonify({'error': 'Invalid file type'}), 400


def enhance_resume(resume_text, missing_keywords):
    prompt = f"Enhance the following resume text by incorporating the following keywords where appropriate and improving the language: {','.join(missing_keywords)}\n\nResume:\n{resume_text}"
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    print("OpenAI API Response:")
    print(response.choices[0].message.content.strip())
    # Check if response has choices and retrieve the enhanced resume text
    if response:
        enhanced_resume_text = response.choices[0].message.content.strip()
        return enhanced_resume_text
    else:
        return "Failed to enhance the resume."



@app.route('/generate-enhanced-resume', methods=['POST'])
def generate_enhanced_resume():
    data = request.get_json()
    resume_filename = data.get('resume_filename')
    job_description = data.get('job_description')

    resume_filepath = os.path.join(app.config['UPLOAD_FOLDER'], resume_filename)
    if not os.path.exists(resume_filepath):
        return jsonify({'error': 'Resume file not found'}), 404

    if resume_filename.endswith('.pdf'):
        resume_text = parse_pdf(resume_filepath)
    elif resume_filename.endswith('.docx'):
        resume_text = parse_docx(resume_filepath)
    else:
        return jsonify({'error': 'Unsupported resume file type'}), 400

    doc = nlp(resume_text)
    resume_keywords = {token.text.lower() for token in doc if not token.is_stop and not token.is_punct}

    job_doc = nlp(job_description)
    job_keywords = {token.text.lower() for token in job_doc if not token.is_stop and not token.is_punct}

    resume_keywords = resume_keywords or set()
    job_keywords = job_keywords or set()

    missing_keywords = job_keywords - resume_keywords

    enhanced_resume_text = enhance_resume(resume_text, missing_keywords)

    enhanced_filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'enhanced_resume.docx')
    doc = Document()
    for line in enhanced_resume_text.split('\n'):
        doc.add_paragraph(line)
    doc.save(enhanced_filepath)

    return send_file(enhanced_filepath, as_attachment=True, download_name='enhanced_resume.docx')


@app.route('/download-enhanced-resume/<filename>', methods=['GET'])
def download_enhanced_resume(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.exists(filepath):
        return jsonify({'error': 'File not found'}), 404

    return send_file(filepath, as_attachment=True, download_name=filename), 200



def get_job_listings(keyword, location):
    url = f"https://www.indeed.com/jobs?q={keyword}&l={location}&vjk=aca28b484413f4df"
    response = requests.get(url)
    print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = []
    # for job in soup.find_all('div', class_='css-dekpa e37uo190'):
    #     title = job.find('ul', class_='css-zu9cdh').text.strip()
    #     company = job.find('span', class_='company').text.strip()
    #     summary = job.find('div', class_='summary').text.strip()
    #     link = job.find('a')['href']
    jobs.append({
        'title': 'Hello Javascript Developer',
        'company': 'Faceebook',
        'summary': 'we are recruiting sooo....',
        # 'link': f"https://www.indeed.com{link}"
    })
    return jobs

@app.route('/joblistings', methods=['GET'])
def job_listings():
    keyword = request.args.get('keyword', 'remote')
    location = request.args.get('location', 'nigeria')
    jobs = get_job_listings(keyword, location)
    return jsonify({'jobs': jobs}), 200

if __name__ == '__main__':
    app.run(debug=True)
