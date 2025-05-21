<template>
  <div>
    <div
      @dragover.prevent="isDragging = true"
      @dragleave="isDragging = false"
      @drop.prevent="handleDrop"
      :class="{
        'border-indigo-300 bg-indigo-50': isDragging,
        'border-gray-300': !isDragging && !file,
        'border-green-300 bg-green-50': file && !isDragging
      }"
      class="mt-1 flex justify-center px-6 pt-5 pb-6 border-2 border-dashed rounded-md transition-colors duration-200"
    >
      <div class="space-y-1 text-center">
        <svg
          :class="{
            'text-indigo-500': isDragging,
            'text-gray-400': !isDragging && !file,
            'text-green-500': file && !isDragging
          }"
          class="mx-auto h-12 w-12"
          stroke="currentColor"
          fill="none"
          viewBox="0 0 48 48"
          aria-hidden="true"
        >
          <path
            d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </svg>
        <div class="flex text-sm text-gray-600">
          <label
            for="file-upload"
            class="relative cursor-pointer rounded-md font-medium text-indigo-600 hover:text-indigo-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-indigo-500"
          >
            <span>Upload a file</span>
            <input
              id="file-upload"
              name="file-upload"
              type="file"
              class="sr-only"
              @change="handleFileChange"
              accept=".pdf,.docx,.txt"
            />
          </label>
          <p class="pl-1">or drag and drop</p>
        </div>
        <p class="text-xs text-gray-500">
          PDF, DOCX, or TXT up to 5MB
        </p>
      </div>
    </div>

    <div v-if="file" class="mt-2 flex items-center justify-between bg-blue-50 p-3 rounded-md">
      <div class="flex items-center">
        <svg class="h-5 w-5 text-blue-500" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd" />
        </svg>
        <span class="ml-2 text-sm font-medium text-gray-900 truncate max-w-xs">
          {{ file.name }}
        </span>
      </div>
      <button
        type="button"
        @click="removeFile"
        class="ml-1 p-1 rounded-full hover:bg-blue-100 focus:outline-none focus:ring-2 focus:ring-blue-500"
      >
        <svg class="h-4 w-4 text-blue-500" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
        </svg>
      </button>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  props: {
    fileType: {
      type: String,
      required: true
    }
  },
  emits: ['file-selected'],
  setup(props, { emit }) {
    const isDragging = ref(false)
    const file = ref(null)

    const handleFileChange = (e) => {
      const selectedFile = e.target.files[0]
      if (selectedFile) {
        file.value = selectedFile
        emit('file-selected', selectedFile)
      }
    }

    const handleDrop = (e) => {
      isDragging.value = false
      const droppedFile = e.dataTransfer.files[0]
      if (droppedFile && (droppedFile.type === 'application/pdf' || 
                         droppedFile.name.endsWith('.docx') || 
                         droppedFile.name.endsWith('.txt'))) {
        file.value = droppedFile
        emit('file-selected', droppedFile)
      }
    }

    const removeFile = () => {
      file.value = null
      emit('file-selected', null)
    }

    return {
      isDragging,
      file,
      handleFileChange,
      handleDrop,
      removeFile
    }
  }
}
</script>