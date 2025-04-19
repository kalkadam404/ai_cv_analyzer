<template>
  <div class="max-w-md mx-auto p-6 bg-white rounded-lg shadow-lg">
    <h2 class="text-2xl font-bold text-center mb-6">Resume Details</h2>
    <div v-if="error">
      <p class="text-red-500">{{ error }}</p>
    </div>
    <div v-else-if="resume">
      <p><strong>Skills:</strong> {{ resume.skills }}</p>
      <p><strong>Education:</strong> {{ resume.education }}</p>
      <p><strong>Experience:</strong> {{ resume.experience }}</p>
      <p><strong>Extracted Text:</strong> {{ resume.extracted_text }}</p>
    </div>
    <div v-else>
      <p>Loading...</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const resume = ref(null);
const error = ref(null);

const { resume_id } = useRoute().params;

onMounted(async () => {
  const token = localStorage.getItem("access_token");
  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/resumes/${resume_id}/`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    resume.value = response.data;
    console.log("Fetched resume details:", resume.value);
  } catch (err) {
    error.value = "Error fetching resume details. Please try again later.";
    console.error(err);
  }
});
</script>
