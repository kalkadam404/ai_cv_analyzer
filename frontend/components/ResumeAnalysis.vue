<template>
  <section class="flex items-center gap-3 px-20 bg-[#F9F9F9] pt-30 pb-30">
    <div class="flex flex-col gap-8" data-aos="fade-right">
      <div
        class="flex items-center gap-2 rounded-xl py-1 px-3 mt-5 bg-gray-100 w-max"
      >
        <img src="../assets/blank.svg" class="w-4 h-4" alt="" />
        Анализ резюме
      </div>
      <div class="font-bold text-5xl">Улучшите своё резюме с помощью ИИ</div>
      <p class="text-gray-400 text-xl font-medium w-[650px]">
        Наш умный анализатор резюме поможет вам выделиться среди других
        кандидатов и повысить шансы на получение работы мечты.
      </p>
      <div class="flex flex-col gap-5">
        <div class="flex items-center gap-3">
          <img src="../assets/selected.svg" alt="" />
          Анализ ключевых навыков и компетенций
        </div>
        <div class="flex items-center gap-3">
          <img src="../assets/selected.svg" alt="" />
          Рекомендации по улучшению структуры и содержания
        </div>
        <div class="flex items-center gap-3">
          <img src="../assets/selected.svg" alt="" />
          Сравнение с требованиями вакансий
        </div>
        <div class="flex items-center gap-3">
          <img src="../assets/selected.svg" alt="" />
          Проверка грамматики и стиля
        </div>
      </div>
    </div>
    <!-- <div
      class="flex flex-col gap-3 bg-white w-[1100px] rounded-xl shadow-lg p-8"
      data-aos="fade-left"
    >
      <div
        class="flex flex-col items-center justify-center gap-3 h-[300px] border-2 border-dashed border-gray-200 rounded-xl py-2"
      >
        <img
          src="../assets/upload.svg"
          alt=""
          class="w-12 h-12 p-2.5 rounded-full bg-gray-100"
        />
        <div class="text-lg">Загрузите своё резюме</div>
        <p class="text-base text-gray-500 font-mono">
          Поддерживаемые форматы: PDF, DOCX, TXT
        </p>
        <input
          ref="fileInput"
          type="file"
          @change="onFileChange"
          accept=".pdf,.docx,.txt"
          class="hidden"
        />
        <button
          @click="triggerFileInput"
          class="bg-black text-white py-1.5 px-4 rounded-[6px] font-medium"
        >
          Выбрать файл
        </button>
      </div>
      <div class="text-xl mt-3">Результаты анализа (внизу пример)</div>
      <div
        class="flex items-center justify-between bg-[#F3F3F3] py-6 px-5 rounded-[8px]"
      >
        <div class="flex items-center gap-3 text-xl font-sans">
          <img src="../assets/warning.svg" alt="" />
          Отсутствуют ключевые навыки
        </div>
        <div class="text-lg font-medium">Исправить</div>
      </div>
      <div
        class="flex items-center justify-between bg-[#F3F3F3] py-6 px-5 rounded-[8px]"
      >
        <div class="flex items-center gap-3 text-xl font-sans">
          <img src="../assets/warning.svg" alt="" />
          Улучшите описание опыта работы
        </div>
        <div class="text-lg font-medium">Исправить</div>
      </div>
      <div
        class="flex items-center justify-between bg-[#F3F3F3] py-4 px-5 rounded-[8px]"
      >
        <div class="flex items-center gap-3 text-xl font-sans">
          <img src="../assets/done.svg" alt="" />
          Хорошая структура резюме
        </div>
      </div>
      <NuxtLink
        to="/Analysis"
        class="bg-black text-center text-white py-2 px-4 rounded-[6px] font-medium mt-3"
      >
        Получить полный анализ
      </NuxtLink>
    </div> -->
    <div
      class="flex flex-col gap-3 bg-white w-[1100px] rounded-xl shadow-lg p-8"
      data-aos="fade-left"
    >
      <div
        :class="[
          'flex flex-col items-center justify-center gap-3 h-[300px] border-2 border-dashed rounded-xl py-2 transition-all',
          fileUploaded
            ? 'border-green-400 bg-green-50 shadow-inner'
            : 'border-gray-200 bg-white',
        ]"
      >
        <img
          :src="fileUploaded ? done : upload"
          alt=""
          class="w-12 h-12 p-2.5 rounded-full"
          :class="fileUploaded ? 'bg-green-100' : 'bg-gray-100'"
        />
        <div class="text-lg">
          {{ fileUploaded ? "Файл загружен успешно" : "Загрузите своё резюме" }}
        </div>
        <p class="text-base text-gray-500 font-mono" v-if="!fileUploaded">
          Поддерживаемые форматы: PDF, DOCX, TXT
        </p>

        <!-- Скрытый input -->
        <input
          ref="fileInput"
          type="file"
          @change="onFileChange"
          accept=".pdf,.docx,.txt"
          class="hidden"
        />

        <!-- Кнопка выбора файла -->
        <button
          @click="triggerFileInput"
          class="bg-black text-white py-1.5 px-4 rounded-[6px] font-medium"
        >
          {{ fileUploaded ? "Заменить файл" : "Выбрать файл" }}
        </button>

        <!-- Имя файла -->
        <div v-if="fileUploaded" class="mt-2 text-sm text-green-600 font-mono">
          {{ uploadedFileName }}
        </div>
      </div>
      <div class="text-xl mt-3">Результаты анализа (внизу пример)</div>
      <div
        class="flex items-center justify-between bg-[#F3F3F3] py-6 px-5 rounded-[8px]"
      >
        <div class="flex items-center gap-3 text-xl font-sans">
          <img src="../assets/warning.svg" alt="" />
          Отсутствуют ключевые навыки
        </div>
        <div class="text-lg font-medium">Исправить</div>
      </div>
      <div
        class="flex items-center justify-between bg-[#F3F3F3] py-6 px-5 rounded-[8px]"
      >
        <div class="flex items-center gap-3 text-xl font-sans">
          <img src="../assets/warning.svg" alt="" />
          Улучшите описание опыта работы
        </div>
        <div class="text-lg font-medium">Исправить</div>
      </div>
      <div
        class="flex items-center justify-between bg-[#F3F3F3] py-4 px-5 rounded-[8px]"
      >
        <div class="flex items-center gap-3 text-xl font-sans">
          <img src="../assets/done.svg" alt="" />
          Хорошая структура резюме
        </div>
      </div>
      <NuxtLink
        to="/Analysis"
        class="bg-black text-center text-white py-2 px-4 rounded-[6px] font-medium mt-3"
      >
        Получить полный анализ
      </NuxtLink>
    </div>
  </section>
</template>

<script setup>
import upload from "../assets/upload.svg";
import done from "../assets/done.svg";
import { ref } from "vue";
import axios from "axios";
const fileInput = ref(null);
const file = ref(null);
const result = ref(null);
const uploadedFileName = ref("");
const fileUploaded = ref(false);
const onFileChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    uploadedFileName.value = file.name;
    fileUploaded.value = true;
  }
};
const triggerFileInput = () => {
  fileInput.value?.click();
};

const uploadResume = async () => {
  const token = localStorage.getItem("access_token");

  const formData = new FormData();
  formData.append("file", file.value);

  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/api/resumes/upload/",
      formData,
      {
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "multipart/form-data",
        },
      }
    );
    result.value = response.data;
    console.log("Resume uploaded successfully:", response.data);
  } catch (error) {
    console.error("Error uploading resume:", error);
  }
};
</script>
