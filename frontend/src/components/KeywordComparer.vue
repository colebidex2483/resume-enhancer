<!-- frontend/src/components/KeywordComparer.vue -->
<template>
    <v-col cols="12" md="12" sm="12">
        <!-- Job Description Input -->
        <v-textarea v-model="jobDescription" label="Enter Job Description" />
    </v-col>
    <v-col cols="12" md="12" sm="12">
        <!-- Resume Upload Input -->
        <div class="upload-container">
    <h3>Upload File</h3>
    <div class="upload-card" @click="triggerFileInput">
      <input
        type="file"
        ref="resumeFile"
        class="file-input"
        @change="handleResumeFileChange"
        accept=".pdf,.jpg,.png"
      />
      <div class="upload-content">
        <img src="" alt="Upload Icon" class="upload-icon" />
        <p>Click To Upload</p>
      </div>
    </div>
  </div>

    </v-col>




   
    <!-- Button to Generate Enhanced Resume -->
    <v-btn color="primary" @click="generateEnhancedResume">Generate Enhanced Resume</v-btn>

</template>

<script setup>
import { ref } from 'vue'

const resumeFile = ref(null)
const jobDescription = ref('')

const handleResumeFileChange = (event) => {
    resumeFile.value = event.target.files[0]
}
const triggerFileInput = () => {
    resumeFile.value.click()
}

const generateEnhancedResume = async () => {
    try {
        const resumeFormData = new FormData()
        resumeFormData.append('resume', resumeFile.value)
        resumeFormData.append('job_description', jobDescription.value) // Include job description in the FormData

        const uploadResumeResponse = await fetch('/api/upload', {
            method: 'POST',
            body: resumeFormData,
        })

        if (uploadResumeResponse.ok) {
            const resumeData = await uploadResumeResponse.json()

            const compareResponse = await fetch('/api/compare', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    resume_filename: resumeData.filename,
                    job_description: jobDescription.value, // Include job description in the comparison request
                }),
            })

            if (compareResponse.ok) {
                const blob = await compareResponse.blob()
                const url = window.URL.createObjectURL(blob)
                const a = document.createElement('a')
                a.style.display = 'none'
                a.href = url
                a.download = 'enhanced_resume.docx'
                document.body.appendChild(a)
                a.click()
                window.URL.revokeObjectURL(url)
            } else {
                console.error('Comparison failed:', compareResponse.statusText)
            }
        } else {
            console.error('Upload failed:', uploadResumeResponse.statusText)
        }
    } catch (error) {
        console.error('Error generating enhanced resume:', error)
    }
}
</script>

<style scoped>
.upload-container {
  text-align: center;
  margin-top: 50px;
}

.upload-card {
  border: 2px dashed #bdbdbd;
  background-color: #e0f7fa;
  padding: 40px 0;
  border-radius: 8px;
  cursor: pointer;
  display: inline-block;
  width: 100%;
  max-width: 400px;
}

.upload-content {
  text-align: center;
}

.upload-icon {
  width: 50px;
  height: 50px;
}

.upload-content p {
  margin-top: 10px;
  font-size: 18px;
  color: #3b82f6;
}

.file-input {
  display: none;
}
</style>