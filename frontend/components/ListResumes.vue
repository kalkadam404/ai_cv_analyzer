<template>
  <div class="max-w-4xl mx-auto p-6 bg-white rounded-lg shadow-lg">
    <h2 class="text-2xl font-bold text-center mb-6">Your Resumes</h2>
    <div v-if="resumes.length === 0" class="text-center text-gray-500">
      No resumes uploaded yet.
    </div>
    <div v-else>
      <ul class="space-y-4">
        <li
          v-for="resume in resumes"
          :key="resume.id"
          class="flex justify-between items-center p-4 bg-gray-100 rounded-md"
        >
          <span>{{ resume.file }}</span>
          <router-link
            :to="`/resumes/${resume.id}`"
            class="text-blue-500 hover:underline"
          >
            View Details
          </router-link>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const resumes = ref([]);

const fetchResumes = async () => {
  const token = localStorage.getItem("access_token");
  try {
    const response = await axios.get("http://127.0.0.1:8000/api/resumes/", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    resumes.value = response.data;
    console.log("Fetched resumes:", resumes.value);
  } catch (error) {
    console.error("Error fetching resumes:", error);
  }
};

onMounted(() => {
  fetchResumes();
});
</script>
