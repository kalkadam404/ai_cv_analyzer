<template>
  <div class="min-h-screen px-6 py-10" data-aos="fade-up">
    <!-- Header -->
    <div class="text-center mb-12">
      <h1 class="text-5xl font-extrabold text-gray-800">Анализ резюме</h1>
      <p class="text-gray-600 text-xl mt-2">
        Улучшите своё резюме с помощью AI
      </p>
    </div>

    <!-- Feedback Section -->
    <div class="bg-white shadow-xl rounded-2xl p-8 mb-12 max-w-5xl mx-auto">
      <h2 class="text-3xl font-bold mb-6 text-black flex items-center gap-2">
        <svg
          class="w-8 h-8 text-black"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M9 12h6m2 4H7m2-8h6M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H7l-2 2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
          />
        </svg>
        Фидбек по резюме
      </h2>

      <div class="mb-6">
        <h3 class="text-lg font-semibold text-red-600 mb-2">
          Навыки, которых не хватает:
        </h3>
        <div class="flex flex-wrap gap-2">
          <span
            v-for="skill in feedback.missing_skills"
            :key="skill"
            class="bg-red-100 text-red-700 px-3 py-1 rounded-full text-sm"
          >
            {{ skill }}
          </span>
        </div>
      </div>

      <div class="mb-6">
        <h3 class="text-lg font-semibold text-blue-600 mb-2">
          Советы по форматированию:
        </h3>
        <p
          class="bg-blue-50 text-blue-700 p-3 rounded-lg border border-blue-100"
        >
          {{ feedback.formatting_feedback }}
        </p>
      </div>

      <div>
        <h3 class="text-lg font-semibold text-green-600 mb-2">
          Рекомендуемые ключевые слова (для ATS):
        </h3>
        <div class="flex flex-wrap gap-2">
          <span
            v-for="keyword in feedback.ats_keywords_suggestion"
            :key="keyword"
            class="bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm"
          >
            {{ keyword }}
          </span>
        </div>
      </div>
    </div>

    <!-- Recommended Jobs -->
    <div class="bg-white shadow-xl rounded-2xl p-8 max-w-6xl mx-auto">
      <h2 class="text-3xl font-bold mb-6 text-black flex items-center gap-2">
        <svg
          class="w-8 h-8 text-black"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M16 7a4 4 0 00-8 0v4H5a1 1 0 000 2h14a1 1 0 000-2h-3V7z"
          />
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 17v.01"
          />
        </svg>
        Рекомендованные вакансии
      </h2>

      <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
        <div
          v-for="job in jobs"
          :key="job.id"
          class="relative bg-gradient-to-r from-white via-gray-50 to-gray-100 p-6 rounded-xl shadow-md hover:shadow-xl transition"
        >
          <h3 class="text-2xl font-bold text-gray-800">{{ job.title }}</h3>
          <p class="text-gray-600 mb-1">
            {{ job.company }} — {{ job.location }}
          </p>
          <p class="text-sm text-gray-500 mb-4 line-clamp-3">
            {{ job.description }}
          </p>
          <p class="text-lg font-semibold text-indigo-700">{{ job.salary }}</p>
          <div
            :class="[
              'absolute text-white px-3 py-1 rounded-full text-sm top-4 right-4 shadow-md',
              getRatingColor(job.match_score),
            ]"
          >
            Совпадение: {{ job.match_score.toFixed(1) }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const jobs = ref([]);
const feedback = ref({
  missing_skills: [],
  formatting_feedback: "",
  ats_keywords_suggestion: [],
});

const getRatingColor = (score) => {
  if (score >= 7) return "bg-green-500";
  if (score >= 5) return "bg-yellow-500";
  return "bg-red-500";
};

onMounted(async () => {
  const token = localStorage.getItem("access_token");
  try {
    // Получение вакансий
    const jobsRes = await axios.get(
      "http://localhost:8000/api/vacancies/matched/2/",
      {
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "multipart/form-data",
        },
      }
    );
    jobs.value = jobsRes.data;
    console.log("Вакансии загружены:", jobs.value);

    // Получение фидбека по резюме (resume_id = 2)
    const feedbackRes = await axios.get(
      "http://localhost:8000/api/resumes/feedback/2/",
      {
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "multipart/form-data",
        },
      }
    );
    feedback.value = feedbackRes.data;
  } catch (error) {
    console.error("Ошибка при загрузке данных:", error);
  }
});
</script>

<style scoped>
.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
