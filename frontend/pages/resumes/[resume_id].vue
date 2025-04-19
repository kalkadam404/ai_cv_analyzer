<template>
  <div class="max-w-md mx-auto p-6 bg-white rounded-lg shadow-lg">
    <h2 class="text-2xl font-bold text-center mb-6">Resume Details</h2>

    <div v-if="error" class="text-red-500">{{ error }}</div>

    <div v-else-if="resume">
      <p><strong>Skills:</strong> {{ resume.skills }}</p>
      <p><strong>Education:</strong> {{ resume.education }}</p>
      <p><strong>Experience:</strong> {{ resume.experience }}</p>
      <p><strong>Extracted Text:</strong> {{ resume.extracted_text }}</p>

      <h3 class="text-xl font-semibold mt-6 mb-2">Matched Vacancies</h3>
      <ul v-if="vacancies.length > 0" class="space-y-2">
        <li
          v-for="vacancy in vacancies"
          :key="vacancy.id"
          class="border p-3 rounded bg-gray-50"
        >
          <p class="font-bold">{{ vacancy.title }} at {{ vacancy.company }}</p>
          <p><strong>Location:</strong> {{ vacancy.location }}</p>
          <p>
            <strong>Salary:</strong> {{ vacancy.salary ?? "Not specified" }}
          </p>
          <p>{{ vacancy.description }}</p>
        </li>
      </ul>
      <p v-else class="text-gray-500">No matched vacancies found.</p>
    </div>

    <div v-else>
      <p>Loading...</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useRoute } from "vue-router";

const resume = ref(null);
const vacancies = ref([]);
const error = ref(null);

const { resume_id } = useRoute().params;

onMounted(async () => {
  const token = localStorage.getItem("access_token");

  try {
    const resumeResponse = await axios.get(
      `http://127.0.0.1:8000/api/resumes/${resume_id}/`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    resume.value = resumeResponse.data;

    const vacanciesResponse = await axios.get(
      `http://127.0.0.1:8000/api/vacancies/recommended/`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    vacancies.value = vacanciesResponse.data;
  } catch (err) {
    error.value = "Error fetching data. Please try again later.";
    console.error(err);
  }
});
</script>
