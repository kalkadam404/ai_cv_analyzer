<template>
  <div class="p-8 max-w-xl mx-auto">
    <h1 class="text-2xl font-bold mb-4">Upload Your Resume</h1>

    <form @submit.prevent="uploadResume">
      <input
        type="file"
        @change="onFileChange"
        accept=".pdf,.docx"
        class="mb-4"
      />
      <button
        class="bg-blue-500 text-white px-4 py-2 rounded"
        :disabled="!file"
      >
        Upload
      </button>
    </form>

    <div v-if="result" class="mt-6 bg-gray-100 p-4 rounded">
      <h2 class="text-xl font-semibold mb-2">Analysis Result</h2>
      <pre class="text-sm whitespace-pre-wrap">{{ result }}</pre>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const file = ref(null);
const result = ref(null);
const { $axios } = useNuxtApp();

const onFileChange = (e) => {
  file.value = e.target.files[0];
};

const uploadResume = async () => {
  if (!file.value) return;

  const formData = new FormData();
  formData.append("resume", file.value);

  try {
    const response = await $axios("/resumes/upload/", {
      method: "POST",
      body: formData,
    });

    result.value = response;
  } catch (err) {
    alert("Upload failed: " + err.message);
  }
};
</script>
