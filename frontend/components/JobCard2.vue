<template>
  <div
    class="flex flex-col gap-4 bg-white rounded-lg border border-gray-300 hover:shadow-md py-3 px-4"
  >
    <p class="text-2xl font-bold">{{ job.title }}</p>
    <div class="flex items-center gap-2 mt-2">
      <img src="../assets/building.svg" alt="" />
      <p class="text-gray-500">{{ job.company }}</p>
    </div>
    <div class="flex items-center gap-20 mt-3">
      <div class="flex items-center gap-2">
        <img src="../assets/location.svg" alt="" />
        <p class="text-gray-500">{{ job.location }}</p>
      </div>
      <div class="flex items-center gap-2">
        <!-- <img src="../assets/dollar.svg" alt="" /> -->
        <p class="text-gray-500">от {{ job.salary }}</p>
      </div>
    </div>
    <div class="flex items-center gap-2 mt-2">
      <button class="text-sm rounded-xl bg-gray-100 font-semibold px-2 py-1">
        React
      </button>
      <button class="text-sm rounded-xl bg-gray-100 font-semibold px-2 py-1">
        TypeScript
      </button>
      <button class="text-sm rounded-xl bg-gray-100 font-semibold px-2 py-1">
        Next.js
      </button>
    </div>
    <button class="w-full py-2 font-bold bg-black text-white rounded-[6px]">
      Анализировать
    </button>
  </div>
</template>

<script setup>
defineProps({
  job: Object,
});
</script>
