<template>
  <div class="min-h-screen">
    <div
      class="flex flex-col items-center justify-center mt-10"
      data-aos="fade-up"
    >
      <div class="font-bold text-4xl">Список вакансий</div>
      <p class="text-slate-500 text-xl font-medium">
        Найдите работу своей мечты среди тысяч вакансий
      </p>
    </div>
    <div class="grid grid-cols-3 gap-4 mt-10 mx-20">
      <JobCard2 v-for="job in jobs" :key="job.id" :job="job" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const jobs = ref([]);

onMounted(async () => {
  try {
    const response = await axios.get("http://localhost:8000/api/vacancies/");
    jobs.value = response.data;
    console.log("Вакансии загружены:", jobs.value);
  } catch (error) {
    console.error("Ошибка при загрузке вакансий:", error);
  }
});
</script>
