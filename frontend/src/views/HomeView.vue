
<template>

  <div class="bg-white">
    <header class="absolute inset-x-0 top-0 z-50">
      <nav class="flex items-center justify-between p-6 lg:px-8" aria-label="Global">
        <div class="flex lg:flex-1">
          <a href="#" class="-m-1.5 p-1.5">
            <span class="sr-only">Your Company</span>
            <img class="h-8 w-auto" src="https://tailwindui.com/plus/img/logos/mark.svg?color=indigo&shade=600" alt="">
          </a>
        </div>
        <div class="flex lg:hidden">
          <button type="button" class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700">
            <span class="sr-only">Open main menu</span>
            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true" data-slot="icon">
              <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
            </svg>
          </button>
        </div>
        <div class="hidden lg:flex lg:gap-x-12">
          <a href="#" class="text-sm font-semibold leading-6 text-gray-900">Product</a>
          <a href="#" class="text-sm font-semibold leading-6 text-gray-900">Features</a>
          <a href="#" class="text-sm font-semibold leading-6 text-gray-900">Marketplace</a>
          <a href="#" class="text-sm font-semibold leading-6 text-gray-900">Company</a>
        </div>
        <div class="hidden lg:flex lg:flex-1 lg:justify-end">
          <a href="#" class="text-sm font-semibold leading-6 text-gray-900">Log in <span aria-hidden="true">&rarr;</span></a>
        </div>
      </nav>
      <!-- Mobile menu, show/hide based on menu open state. -->
      <div class="lg:hidden" role="dialog" aria-modal="true">
        <!-- Background backdrop, show/hide based on slide-over state. -->
        <div class="fixed inset-0 z-50"></div>
        <div class="fixed inset-y-0 right-0 z-50 w-full overflow-y-auto bg-white px-6 py-6 sm:max-w-sm sm:ring-1 sm:ring-gray-900/10">
          <div class="flex items-center justify-between">
            <a href="#" class="-m-1.5 p-1.5">
              <span class="sr-only">Your Company</span>
              <img class="h-8 w-auto" src="https://tailwindui.com/plus/img/logos/mark.svg?color=indigo&shade=600" alt="">
            </a>
            <button type="button" class="-m-2.5 rounded-md p-2.5 text-gray-700">
              <span class="sr-only">Close menu</span>
              <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true" data-slot="icon">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18 18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
          <div class="mt-6 flow-root">
            <div class="-my-6 divide-y divide-gray-500/10">
              <div class="space-y-2 py-6">
                <a href="#" class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">Product</a>
                <a href="#" class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">Features</a>
                <a href="#" class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">Marketplace</a>
                <a href="#" class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">Company</a>
              </div>
              <div class="py-6">
                <a href="#" class="-mx-3 block rounded-lg px-3 py-2.5 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">Log in</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
  
    <div class="relative isolate px-6 pt-14 lg:px-8">
      <div class="absolute inset-x-0 -top-40 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80" aria-hidden="true">
        <div class="relative left-[calc(50%-11rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 rotate-[30deg] bg-gradient-to-tr from-[#ff80b5] to-[#9089fc] opacity-30 sm:left-[calc(50%-30rem)] sm:w-[72.1875rem]" style="clip-path: polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)"></div>
      </div>
      <div class="mx-auto max-w-2xl py-32 sm:py-48 lg:py-56">
        <div class="hidden sm:mb-8 sm:flex sm:justify-center">
          <div class="relative rounded-full px-3 py-1 text-sm leading-6 text-gray-600 ring-1 ring-gray-900/10 hover:ring-gray-900/20">
            Announcing our next round of funding. <a href="#" class="font-semibold text-indigo-600"><span class="absolute inset-0" aria-hidden="true"></span>Read more <span aria-hidden="true">&rarr;</span></a>
          </div>
        </div>
        <div class="text-center">
          <h1 class="text-balance text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl">Data to enrich your online business</h1>
          <p class="mt-6 text-lg leading-8 text-gray-600">Anim aute id magna aliqua ad ad non deserunt sunt. Qui irure qui lorem cupidatat commodo. Elit sunt amet fugiat veniam occaecat fugiat aliqua.</p>
          <div class="mt-10 flex items-center justify-center gap-x-6">
            <a href="#" class="rounded-md bg-indigo-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Get started</a>
            <a href="#" class="text-sm font-semibold leading-6 text-gray-900">Learn more <span aria-hidden="true">→</span></a>
          </div>
        </div>
      </div>
      <div class="absolute inset-x-0 top-[calc(100%-13rem)] -z-10 transform-gpu overflow-hidden blur-3xl sm:top-[calc(100%-30rem)]" aria-hidden="true">
        <div class="relative left-[calc(50%+3rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 bg-gradient-to-tr from-[#ff80b5] to-[#9089fc] opacity-30 sm:left-[calc(50%+36rem)] sm:w-[72.1875rem]" style="clip-path: polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)"></div>
      </div>
    </div>
  </div>
  
  
    <!-- <v-container>
      <v-col cols="12" md="12" sm="12"> -->
          <!-- Job Description Input -->
          <!-- <v-textarea v-model="jobDescription" label="Enter Job Description" />
      </v-col>
  
      <v-btn color="primary" @click="getAlljoblisting">get all job listing</v-btn>
  {{ listing }}
      <div class=" w-[428px] mx-auto pt-5">
        <form @submit.prevent="onSubmit" enctype="multipart/form-data" class="mb-11">
  
          <label for="cac_file" class="text-base font-Nunito-Sans font-normal">
            File format supported PDF/JPG/PNG -->
  
            <!-- ************************************************** -->
            <!--Display this section if file is not selected
                        i did this so that the delete icon can work-->
            <!-- ************************************************** -->
            <!-- <div v-if="!selectedFile"
              class=" bg-white flex justify-center mt-1 items-center cursor-pointer h-36 rounded-lg border border-solid border-[#E5E5E5]">
  
              <input type="file" id="cac_file" name="cac_file" @change="handleFileChange"
                class="bg-[#F4F4F4] w-[100%] hidden outline-1 text-sm pl-2 font-normal my-2 rounded-md placeholder-[#ABABAB] h-12 hover:bg-white focus:bg-white md:hover:drop-shadow-lg outline-none" />
              <span class="flex items-center gap-[16px]">
                <Icons name="uploadicon" />
                <v-icon size="30px" class="w-[40px] h-[40px]" color="#006033"> 
                  mdi-upload
                </v-icon>
                Click to upload your resume
              </span>
  
            </div>
          </label> -->
  
  
          <!-- ************************************************** -->
          <!--Display this section if file is selected  -->
          <!-- ************************************************** -->
          <!-- <div v-if="selectedFile"
            class=" bg-white w-[428px] flex justify-center mt-[20px] items-center h-[145px] rounded-[10px] border border-solid border-[#E5E5E5]">
  
            <div v-if="selectedFile" class="px-14 w-[100%] font-normal">
              <div class="flex justify-between mb-5">
                <span class="font-normal text-sm">
                  <Icons name="file" class="mr-1 inline-block" />
                  {{ selectedFile.name }}
                </span>
                <div>
                  <v-icon size="25px" color="red" @click="selectedFile = null"> 
                  mdi-delete
                </v-icon>
                </div>
              </div>
  
              <p>
                <v-icon size="30px" class="mr-1 inline" color="green" @click="selectedFile = null"> 
                  mdi-check-all
                </v-icon>
                <Icons name="uploaded-mark" class="mr-1 inline" />
                <span class="font-normal text-sm">File uploaded</span>
              </p>
            </div>
  
          </div>
          
          <v-btn :disabled="!selectedFile" color="primary" class="mt-[28px] font-bold w-[428px]" :loading="loading" @click="onSubmit">Upload Resume</v-btn>
    
        </form>
        <v-btn color="primary" @click="generateEnhancedResume">Generate Enhanced Resume</v-btn>
      </div> -->
  
  
      <!-- <div v-if="parsedResume">
        <v-divider class="my-4"></v-divider>
        <v-card>
          <v-card-title>Parsed Resume Text</v-card-title>
          <v-card-text>
            <pre>{{ parsedResume }}</pre>
          </v-card-text>
        </v-card>
  
        <v-divider class="my-4"></v-divider>
        <v-card>
          <v-card-title>Entities</v-card-title>
          <v-card-text>
            <v-list>
              <v-list-item v-for="entity in entities" :key="entity.text">
                <v-list-item-content>
                  <v-list-item-title>{{ entity.label }}</v-list-item-title>
                  <v-list-item-subtitle>{{ entity.text }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>
  
        <v-divider class="my-4"></v-divider>
        <v-card>
          <v-card-title>Keywords</v-card-title>
          <v-card-text>
            <v-list>
              <v-list-item v-for="keyword in keywords" :key="keyword">
                <v-list-item-content>{{ keyword }}</v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>
  
        <v-divider class="my-4"></v-divider>
        <v-card>
          <v-card-title>Readability Scores</v-card-title>
          <v-card-text>
            <p><strong>Polarity:</strong> {{ sentiment.polarity }}</p>
            <p><strong>Subjectivity:</strong> {{ sentiment.subjectivity }}</p>
          </v-card-text>
        </v-card>
      </div>
    </v-container> -->
  </template>
  
  <script setup>
  import { ref } from 'vue';
  const jobDescription = ref('')
  const parsedResume = ref('');
  const entities = ref([]);
  const listing = ref({});
  const keywords = ref([]);
  const sentiment = ref({ polarity: 0, subjectivity: 0 });
  const selectedFile = ref(null);
  const loading = ref(false);
  
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    selectedFile.value = file;
  };
  
  const onSubmit = async () => {
    loading.value = true
    try {
      
      const formData = new FormData();
      formData.append('resume', selectedFile.value);
  
      const response = await fetch('/api/upload', {
        method: 'POST',
        body: formData,
      });
  
      if (response.ok) {
        loading.value = false
        const data = await response.json();
        const analyzeResponse = await fetch(`/api/analyze/${data.filename}`);
        const analyzeData = await analyzeResponse.json();
        parsedResume.value = analyzeData.resume_text;
        entities.value = analyzeData.entities;
        keywords.value = analyzeData.keywords;
        sentiment.value = analyzeData.sentiment;
      } else {
        console.error('Upload failed:', response.statusText);
      }
    } catch (error) {
      console.error('Error uploading resume:', error);
    }
  };
  const getAlljoblisting = async () => {
    loading.value = true
    try {
  
      const response = await fetch('/api/joblistings', {
        method: 'GET',
      });
  
      if (response.ok) {
  
        loading.value = false
        const data = await response.json();
        listing.value = data
  
      } else {
        console.error('Upload failed:', response.statusText);
      }
    } catch (error) {
      console.error('Error uploading resume:', error);
    }
  };
  
  
  
  const generateEnhancedResume = async () => {
      try {
          const resumeFormData = new FormData()
          resumeFormData.append('resume', selectedFile.value)
          resumeFormData.append('job_description', jobDescription.value) // Include job description in the FormData
  
          const uploadResumeResponse = await fetch('/api/upload', {
              method: 'POST',
              body: resumeFormData,
          })
  
          if (uploadResumeResponse.ok) {
              const resumeData = await uploadResumeResponse.json()
  
              const compareResponse = await fetch('/api/generate-enhanced-resume', {
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
  .my-4 {
    margin-top: 16px;
    margin-bottom: 16px;
  }
  </style>
  
  https://www.youtube.com/watch?v=8d8YTLhzV50&t=96s