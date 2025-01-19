<template>
    <div>
      <input type="file" @change="handleFileChange" />
      <button @click="uploadResume">Upload Resume</button>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    // Optionally, you can store the file in a ref or reactive state
    // to later pass it to the upload function
  };
  
  const uploadResume = async () => {
    try {
      const formData = new FormData();
      formData.append('resume', file); // Ensure 'file' is properly defined
  
      const response = await fetch('/api/upload', {
        method: 'POST',
        body: formData,
      });
  
      if (response.ok) {
        const data = await response.json();
        console.log('Uploaded successfully:', data);
        // Handle response data (e.g., display enhancement suggestions)
      } else {
        console.error('Upload failed:', response.statusText);
      }
    } catch (error) {
      console.error('Error uploading resume:', error);
    }
  };
  </script>
  