<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-800 to-gray-700 py-10 px-4 sm:px-6 lg:px-8">
    <div class="mx-auto">
      <!-- Header with glowing effect -->
      <div class="text-center mb-12">
        <h1
          class="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 to-purple-600 sm:text-5xl mb-3">
          Corehotech Career Toolkit
        </h1>
        <p class="text-xl text-gray-300">
          AI-powered tools to boost your job applications
        </p>
      </div>

      <!-- Tab Navigation -->
      <div class="mb-6 sm:mb-8 flex justify-center">
        <div class="inline-flex rounded-md bg-gray-800 p-1 shadow-lg w-full sm:w-auto">
          <button @click="activeTab = 'resume'" :class="{
            'bg-indigo-600 text-white': activeTab === 'resume',
            'text-gray-300 hover:text-white': activeTab !== 'resume'
          }"
            class="px-4 py-2 sm:px-6 sm:py-3 rounded-md text-sm font-medium transition-all duration-300 w-1/2 sm:w-auto text-center">
            <span class="flex items-center justify-center sm:justify-start">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1 sm:mr-2" viewBox="0 0 20 20"
                fill="currentColor">
                <path fill-rule="evenodd"
                  d="M6 2a2 2 0 00-2 2v12a2 2 0 002 2h8a2 2 0 002-2V7.414A2 2 0 0015.414 6L12 2.586A2 2 0 0010.586 2H6zm2 10a1 1 0 10-2 0 1 1 0 002 0zm2-3a1 1 0 011 1v5a1 1 0 11-2 0v-5a1 1 0 011-1zm4-1a1 1 0 10-2 0v6a1 1 0 102 0V8z"
                  clip-rule="evenodd" />
              </svg>
              <span class="hidden sm:inline">Resume Enhancer</span>
              <span class="sm:hidden">Resume</span>
            </span>
          </button>
          <button @click="activeTab = 'upwork'" :class="{
            'bg-indigo-600 text-white': activeTab === 'upwork',
            'text-gray-300 hover:text-white': activeTab !== 'upwork'
          }"
            class="px-4 py-2 sm:px-6 sm:py-3 rounded-md text-sm font-medium transition-all duration-300 w-1/2 sm:w-auto text-center">
            <span class="flex items-center justify-center sm:justify-start">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1 sm:mr-2" viewBox="0 0 20 20"
                fill="currentColor">
                <path
                  d="M10.394 2.08a1 1 0 00-.788 0l-7 3a1 1 0 000 1.84L5.25 8.051a.999.999 0 01.356-.257l4-1.714a1 1 0 11.788 1.838L7.667 9.088l1.94.831a1 1 0 00.787 0l7-3a1 1 0 000-1.838l-7-3zM3.31 9.397L5 10.12v4.102a8.969 8.969 0 00-1.05-.174 1 1 0 01-.89-.89 11.115 11.115 0 01.25-3.762zM9.3 16.573A9.026 9.026 0 007 14.935v-3.957l1.818.78a3 3 0 002.364 0l5.508-2.361a11.026 11.026 0 01.25 3.762 1 1 0 01-.89.89 8.968 8.968 0 00-5.35 2.524 1 1 0 01-1.4 0zM6 18a1 1 0 001-1v-2.065a8.935 8.935 0 00-2-.712V17a1 1 0 001 1z" />
              </svg>
              <span class="hidden sm:inline">Upwork Proposal</span>
              <span class="sm:hidden">Upwork</span>
            </span>
          </button>
        </div>
      </div>

      <!-- Resume Enhancer Tab -->
      <div v-if="activeTab === 'resume'"
        class="bg-gray-800  bg-opacity-50 backdrop-blur-lg rounded-xl shadow-2xl p-6 mb-8 border border-gray-100 transition-all duration-500">
        <div class="flex flex-col md:flex-row gap-x-8">
          <div class="flex-1">
            <h2 class="text-xl font-medium text-white mb-7 flex items-center">
              <span class="bg-indigo-600 p-2 rounded-lg mr-3">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd"
                    d="M6 2a2 2 0 00-2 2v12a2 2 0 002 2h8a2 2 0 002-2V7.414A2 2 0 0015.414 6L12 2.586A2 2 0 0010.586 2H6zm2 10a1 1 0 10-2 0 1 1 0 002 0zm2-3a1 1 0 011 1v5a1 1 0 11-2 0v-5a1 1 0 011-1zm4-1a1 1 0 10-2 0v6a1 1 0 102 0V8z"
                    clip-rule="evenodd" />
                </svg>
              </span>
              Your Resume
            </h2>
            <FileUpload fileType="resume" @file-selected="handleResumeSelected" />
          </div>

          <div class="flex-1">
            <div class="flex mt-0 flex-col md:flex-row gap-x-5">
              <h2 class="text-xl font-medium text-white mb-4 flex items-center">
                <span class="bg-indigo-600 p-2 rounded-lg mr-3">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9 2a1 1 0 000 2h2a1 1 0 100-2H9z" />
                    <path fill-rule="evenodd"
                      d="M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z"
                      clip-rule="evenodd" />
                  </svg>
                </span>
                Job Description
              </h2>
  
              <div class="flex mb-4">
                <button @click="jobInputMode = 'text'" :class="{
                  'bg-indigo-600 text-white': jobInputMode === 'text',
                  'bg-gray-700 text-gray-300 hover:bg-gray-600': jobInputMode !== 'text'
                }"
                  class="px-4 py-2 rounded-l-md text-sm font-medium focus:outline-none focus:ring-2 focus:ring-indigo-500 transition-colors duration-200">
                  Paste Text
                </button>
                <button @click="jobInputMode = 'file'" :class="{
                  'bg-indigo-600 text-white': jobInputMode === 'file',
                  'bg-gray-700 text-gray-300 hover:bg-gray-600': jobInputMode !== 'file'
                }"
                  class="px-4 py-2 rounded-r-md text-sm font-medium focus:outline-none focus:ring-2 focus:ring-indigo-500 transition-colors duration-200">
                  Upload File
                </button>
              </div>
            </div>

            <div v-if="jobInputMode === 'text'" class="mt-2">
              <textarea id="job-description" v-model="jobDescriptionText" rows="8"
                class="bg-gray-700 h-64 text-gray-200 shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border border-gray-600 rounded-md p-3 placeholder-gray-400"
                placeholder="Paste the job description here..."></textarea>
            </div>

            <div v-if="jobInputMode === 'file'" class="mt-2">
              <FileUpload fileType="job" @file-selected="handleJobSelected" />
            </div>


            <div class="mt-3 flex justify-start ">
              <button @click="enhanceResume" :disabled="!canSubmitResume" :class="{
                'bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 shadow-lg': canSubmitResume,
                'bg-gray-600 cursor-not-allowed': !canSubmitResume
              }"
                class="inline-flex items-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-all duration-300 transform hover:scale-105">
                <span v-if="!isLoading">Enhance My Resume</span>
                <span v-else>Processing...</span>
                <svg v-if="isLoading" class="animate-spin -mr-1 ml-3 h-5 w-5 text-white"
                  xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                  <path class="opacity-75" fill="currentColor"
                    d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z">
                  </path>
                </svg>
              </button>
            </div>
          </div>
        </div>

      </div>

      <!-- Upwork Proposal Tab -->
      <div v-if="activeTab === 'upwork'"
        class="bg-gray-800 bg-opacity-50 backdrop-blur-lg rounded-xl shadow-2xl p-6 mb-8 border border-gray-700 transition-all duration-500">
        <div class="flex flex-col md:flex-row gap-x-4">
          <div class="mb-8 flex-1">
            <h2 class="text-xl font-medium text-white mb-4 flex items-center">
              <span class="bg-indigo-600 p-2 rounded-lg mr-3">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M9 2a1 1 0 000 2h2a1 1 0 100-2H9z" />
                  <path fill-rule="evenodd"
                    d="M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z"
                    clip-rule="evenodd" />
                </svg>
              </span>
              Job Description
            </h2>
            <textarea v-model="upworkJobDescription" rows="6"
              class="bg-gray-700 text-gray-200 shadow-sm h-64 focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border border-gray-600 rounded-md p-3 placeholder-gray-400"
              placeholder="Paste the Upwork job description here..."></textarea>
          </div>

          <div class="mb-8 flex-1">
            <h2 class="text-xl font-medium text-white mb-4 flex items-center">
              <span class="bg-indigo-600 p-2 rounded-lg mr-3">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd"
                    d="M6 2a2 2 0 00-2 2v12a2 2 0 002 2h8a2 2 0 002-2V7.414A2 2 0 0015.414 6L12 2.586A2 2 0 0010.586 2H6zm5 6a1 1 0 10-2 0v3.586l-1.293-1.293a1 1 0 10-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L11 11.586V8z"
                    clip-rule="evenodd" />
                </svg>
              </span>
              Your Proposal Template
            </h2>
            <textarea v-model="upworkProposalTemplate" rows="8"
              class="scroll-box bg-gray-700 text-gray-200 h-64 shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border border-gray-600 rounded-md p-3 placeholder-gray-400"
              placeholder="Enter your proposal template. You can include placeholders like [ClientName], [YourName], etc."></textarea>
            <p class="mt-2 text-sm text-gray-400">Tip: Use placeholders like [ClientName], [YourName], [YourExperience]
              that will be automatically replaced.</p>

            <div class="mt-3 flex md:justify-center justify-start">
              <button @click="generateProposal" :disabled="!canSubmitProposal" :class="{
                'bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 shadow-lg': canSubmitProposal,
                'bg-gray-600 cursor-not-allowed': !canSubmitProposal
              }"
                class="inline-flex items-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-all duration-300 transform hover:scale-105">
                <span v-if="!isLoadingProposal">Generate Proposal</span>
                <span v-else>Generating...</span>
                <svg v-if="isLoadingProposal" class="animate-spin -mr-1 ml-3 h-5 w-5 text-white"
                  xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                  <path class="opacity-75" fill="currentColor"
                    d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z">
                  </path>
                </svg>
              </button>
            </div>
          </div>
        </div>


        <!-- Proposal Result -->
        <div v-if="generatedProposal" class="mt-8 flex-1 bg-gray-900 rounded-lg p-6 border border-gray-700">
          <div class="flex justify-between items-center mb-4">
            <h3 class="text-lg font-medium text-white">Your Custom Proposal</h3>
            <button @click="copyProposal" class="text-indigo-400 hover:text-indigo-300 flex items-center text-sm">
              <svg v-if="showToast == 'Copy'" xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1" fill="none"
                viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" />
              </svg>
              <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24"
                stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
              </svg>

              {{ showToast }}
            </button>
          </div>
          <div class="bg-gray-800 p-4 rounded-md">
            <pre class="text-gray-300 whitespace-pre-wrap">{{ generatedProposal }}</pre>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue'
import axios from 'axios'
import FileUpload from '@/components/FileUpload.vue'

const API_BASE_URL = 'https://resume-enhancer-6en2.onrender.com/api';

export default {
  components: {
    FileUpload
  },
  setup() {
    const activeTab = ref('resume')
    const showToast = ref('Copy')
    // Resume Enhancer State
    const resumeFile = ref(null)
    const jobFile = ref(null)
    const jobInputMode = ref('text')
    const jobDescriptionText = ref('')
    const isLoading = ref(false)

    // Upwork Proposal State
    const upworkJobDescription = ref('')
    const upworkProposalTemplate = ref(`Hi,

I have carefully reviewed the job description and its requirements and understand that you want to [JobDescriptionSummary].

With [YourExperience] years of experience in [RelevantSkills], I believe I possess the qualities and skills needed to get the job done perfectly.

How I’ll Approach the Project:
1. [ApproachStep1]
2. [ApproachStep2]
3. [ApproachStep3]

Relevant Work Samples:
1. [SampleURL1]
2. [SampleURL2]

I have extensive experience in [RelevantSkills] and would love to bring your project to life. Let’s discuss further!

Best regards,

[YourName]
[YourRole] | [YourTopSkills]
`)
    const generatedProposal = ref('')
    const isLoadingProposal = ref(false)

    const handleResumeSelected = (file) => {
      resumeFile.value = file
    }

    const handleJobSelected = (file) => {
      jobFile.value = file
    }

    const canSubmitResume = computed(() => {
      if (!resumeFile.value) return false
      if (jobInputMode.value === 'text') {
        return jobDescriptionText.value.trim().length > 0
      } else {
        return jobFile.value !== null
      }
    })

    const canSubmitProposal = computed(() => {
      return upworkJobDescription.value.trim().length > 0 &&
        upworkProposalTemplate.value.trim().length > 0
    })

    const enhanceResume = async () => {
      if (!canSubmitResume.value) return;

      isLoading.value = true;

      try {
        const formData = new FormData();
        formData.append('resume', resumeFile.value);

        if (jobInputMode.value === 'text') {
          formData.append('job_description_text', jobDescriptionText.value);
        } else {
          formData.append('job_description_file', jobFile.value);
        }

        const response = await axios.post(`${API_BASE_URL}/enhance-resume`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          },
          responseType: 'blob'
        });

        const blob = new Blob([response.data], {
          type: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        });
        const downloadUrl = window.URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = downloadUrl;
        link.setAttribute('download', `enhanced_resume_${new Date().toISOString().split('T')[0]}.docx`);
        document.body.appendChild(link);
        link.click();
        link.remove();

      } catch (err) {
        console.error('Error enhancing resume:', err);
      } finally {
        isLoading.value = false;
      }
    }

    const generateProposal = async () => {
      if (!canSubmitProposal.value) return;

      isLoadingProposal.value = true;
      generatedProposal.value = '';

      try {
        const response = await axios.post(`${API_BASE_URL}/generate-proposal`, {
          job_description: upworkJobDescription.value,
          proposal_template: upworkProposalTemplate.value
        });

        generatedProposal.value = response.data.proposal;
      } catch (err) {
        console.error('Error generating proposal:', err);
      } finally {
        isLoadingProposal.value = false;
      }
    }

    const copyProposal = () => {
      navigator.clipboard.writeText(generatedProposal.value)
        .then(() => {
          // You can add a toast notification here if you want

          showToast.value = 'Copied'
          setTimeout(() => {
            showToast.value = 'Copy'
          }, 3000)
        })
        .catch(err => {
          console.error('Failed to copy proposal:', err);
        });
    }

    return {
      activeTab,
      resumeFile,
      jobFile,
      showToast,
      jobInputMode,
      jobDescriptionText,
      isLoading,
      canSubmitResume,
      enhanceResume,
      handleResumeSelected,
      handleJobSelected,
      upworkJobDescription,
      upworkProposalTemplate,
      generatedProposal,
      isLoadingProposal,
      canSubmitProposal,
      generateProposal,
      copyProposal
    }
  }
}
</script>

<style>
/* Add some futuristic animations */
button {
  transition: all 0.3s ease;
}

.bg-gradient-to-br {
  background-image: linear-gradient(to bottom right, var(--tw-gradient-stops));
}

.backdrop-blur-lg {
  backdrop-filter: blur(16px);
}

.shadow-2xl {
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
}

/* Glowing effect on hover */
.hover-glow:hover {
  box-shadow: 0 0 15px rgba(99, 102, 241, 0.5);
}

/* Scrollbar Track */
.scroll-box::-webkit-scrollbar {
  width: 6px;
}

/* Scrollbar Thumb */
.scroll-box::-webkit-scrollbar-thumb {
  background: linear-gradient(180deg, #6366f1, #22d3ee); /* Green to cyan */
  border-radius: 10px;
}

/* Scrollbar Track */
.scroll-box::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.05); 
  border-radius: 10px;
}

/* Firefox */
.scroll-box {
  scrollbar-width: thin;
  scrollbar-color: #6366f1 rgba(255, 255, 255, 0.05);
}
</style>