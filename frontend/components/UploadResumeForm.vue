<template>
  <div class="bg-black text-white p-6 rounded-xl shadow-md w-full max-w-md">
    <form @submit.prevent="handleUpload" class="space-y-4">
      <input
        type="file"
        accept=".pdf"
        @change="handleFileChange"
        class="w-full border border-gray-300 p-2 rounded bg-white text-black"
      />
      <button
        type="submit"
        class="bg-white text-black font-semibold py-2 px-4 rounded hover:bg-gray-200 transition"
      >
        Upload Resume
      </button>
    </form>

    <div v-if="uploaded" class="mt-4 text-green-400">
      ✅ Resume uploaded successfully!
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
const uploaded = ref(false);
const file = ref(null);

const handleFileChange = (event) => {
  file.value = event.target.files[0];
  console.log("File selected:", file.value); // Лог для проверки
};

const handleUpload = async () => {
  console.log("Upload started"); // Лог для проверки вызова функции
  if (!file.value) {
    console.error("No file selected");
    return;
  }

  const token = localStorage.getItem("access_token");
  if (!token) {
    console.error("No access token found");
    return;
  }

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

    console.log("Response:", response.data); // Логируем ответ сервера
    uploaded.value = true;
  } catch (err) {
    console.error("Upload failed:", err);
  }
};
</script>
