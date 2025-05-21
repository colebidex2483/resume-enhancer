<template>
  <div class="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl mx-auto">
      <div class="text-center mb-12">
        <h1 class="text-3xl font-extrabold text-gray-900 sm:text-4xl">
          Resume Enhancer
        </h1>
        <p class="mt-3 text-xl text-gray-600">
          Upload your resume and provide a job description to get a perfectly tailored CV
        </p>
      </div>

      <div class="bg-white shadow rounded-lg p-6 mb-8">
        <!-- Resume Upload Section -->
        <div class="mb-8">
          <h2 class="text-lg font-medium text-gray-900 mb-4">Your Resume</h2>
          <FileUpload
            fileType="resume"
            @file-selected="handleResumeSelected"
          />
        </div>

        <!-- Job Description Section -->
        <div>
          <h2 class="text-lg font-medium text-gray-900 mb-4">Job Description</h2>
          
          <!-- Toggle between text input and file upload -->
          <div class="flex mb-4">
            <button
              @click="jobInputMode = 'text'"
              :class="{
                'bg-indigo-600 text-white': jobInputMode === 'text',
                'bg-gray-200 text-gray-700': jobInputMode !== 'text'
              }"
              class="px-4 py-2 rounded-l-md text-sm font-medium focus:outline-none focus:ring-2 focus:ring-indigo-500"
            >
              Paste Text
            </button>
            <button
              @click="jobInputMode = 'file'"
              :class="{
                'bg-indigo-600 text-white': jobInputMode === 'file',
                'bg-gray-200 text-gray-700': jobInputMode !== 'file'
              }"
              class="px-4 py-2 rounded-r-md text-sm font-medium focus:outline-none focus:ring-2 focus:ring-indigo-500"
            >
              Upload File
            </button>
          </div>

          <!-- Text Input Mode -->
          <div v-if="jobInputMode === 'text'" class="mt-2">
            <label for="job-description" class="block text-sm font-medium text-gray-700 mb-1">
              Paste the job description below
            </label>
            <textarea
              id="job-description"
              v-model="jobDescriptionText"
              rows="8"
              class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border border-gray-300 rounded-md p-3"
              placeholder="Paste the job description here..."
            ></textarea>
            <p class="mt-1 text-sm text-gray-500">
              You can copy-paste from a job posting or type directly
            </p>
          </div>

          <!-- File Upload Mode -->
          <div v-if="jobInputMode === 'file'" class="mt-2">
            <FileUpload
              fileType="job"
              @file-selected="handleJobSelected"
            />
          </div>
        </div>

        <div class="mt-8 flex justify-center">
          <button
            @click="enhanceResume"
            :disabled="!canSubmit"
            :class="{
              'bg-indigo-600 hover:bg-indigo-700': canSubmit,
              'bg-gray-400 cursor-not-allowed': !canSubmit
            }"
            class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md shadow-sm text-white focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-colors duration-200"
          >
            <span v-if="!isLoading">Enhance My Resume</span>
            <span v-else>Processing...</span>
            <svg v-if="isLoading" class="animate-spin -mr-1 ml-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
          </button>
        </div>
      </div>

      <!-- Results Section (same as before) -->
      <!-- ... -->
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue'
import axios from 'axios'
import FileUpload from '@/components/FileUpload.vue'
const API_BASE_URL = 'http://127.0.0.1:5000/api';
export default {
  components: {
    FileUpload
  },
  setup() {
    const resumeFile = ref(null)
    const jobFile = ref(null)
    const jobInputMode = ref('text') // 'text' or 'file'
    const jobDescriptionText = ref('')
    const enhancedResume = ref(null)
    const isLoading = ref(false)
    const error = ref(null)
    const enhancements = ref([
      'Incorporated keywords from the job description',
      'Highlighted relevant skills and experiences',
      'Optimized language to match job requirements',
      'Improved overall structure and readability'
    ])

    const handleResumeSelected = (file) => {
      resumeFile.value = file
    }

    const handleJobSelected = (file) => {
      jobFile.value = file
    }

    const canSubmit = computed(() => {
      if (!resumeFile.value) return false
      
      if (jobInputMode.value === 'text') {
        return jobDescriptionText.value.trim().length > 0
      } else {
        return jobFile.value !== null
      }
    })

    const enhanceResume = async () => {
      if (!canSubmit.value) return

      isLoading.value = true
      error.value = null

      try {
        const formData = new FormData()
        formData.append('resume', resumeFile.value)

        // Add job description based on input mode
        if (jobInputMode.value === 'text') {
          formData.append('job_description_text', jobDescriptionText.value)
        } else {
          formData.append('job_description_file', jobFile.value)
        }

       const response = await axios.post(`${API_BASE_URL}/enhance-resume`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          },
          responseType: 'blob'
        })

        // Create a preview of the enhanced resume
        const text = await response.data.text()
        const preview = text.length > 500 ? text.substring(0, 500) + '...' : text

        // Create download URL
        const blob = new Blob([text], { type: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' })
        const downloadUrl = URL.createObjectURL(blob)

        enhancedResume.value = {
          downloadUrl,
          preview,
          filename: `enhanced_resume_${new Date().toISOString().split('T')[0]}.docx`
        }
      } catch (err) {
        console.error('Error enhancing resume:', err)
        if (err.response && err.response.data) {
          const reader = new FileReader()
          reader.onload = () => {
            try {
              const errorData = JSON.parse(reader.result)
              error.value = errorData.error || 'Failed to enhance resume'
            } catch (e) {
              error.value = 'Failed to enhance resume'
            }
          }
          reader.readAsText(err.response.data)
        } else {
          error.value = err.message || 'Failed to enhance resume'
        }
      } finally {
        isLoading.value = false
      }
    }

    return {
      resumeFile,
      jobFile,
      jobInputMode,
      jobDescriptionText,
      enhancedResume,
      isLoading,
      error,
      enhancements,
      handleResumeSelected,
      handleJobSelected,
      canSubmit,
      enhanceResume
    }
  }
}
</script>