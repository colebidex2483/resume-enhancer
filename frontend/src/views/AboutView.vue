<!-- frontend/src/components/ResumeParser.vue -->
<template>
  <v-container>

    <div class=" w-[428px] mx-auto pt-5">
      <form @submit.prevent="onSubmit" enctype="multipart/form-data" class="mb-11">

        <label for="cac_file" class="text-base font-Nunito-Sans font-normal">
          File format supported PDF/JPG/PNG

          <!-- ************************************************** -->
          <!--Display this section if file is not selected
                      i did this so that the delete icon can work-->
          <!-- ************************************************** -->
          <div v-if="!selectedFile"
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
        </label>


        <!-- ************************************************** -->
        <!--Display this section if file is selected  -->
        <!-- ************************************************** -->
        <div v-if="selectedFile"
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
        {{ !selectedFile }}
        {{ loading }}
        <v-btn :disabled="!selectedFile" color="primary" class="mt-[28px] font-bold w-[428px]" :loading="loading" @click="onSubmit">Upload Resume</v-btn>
  
      </form>

    </div>


    <div v-if="parsedResume">
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
  </v-container>
</template>

<script setup>
import { ref } from 'vue';

const parsedResume = ref('');
const entities = ref([]);
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

</script>

<style scoped>
.my-4 {
  margin-top: 16px;
  margin-bottom: 16px;
}
</style>
