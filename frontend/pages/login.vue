<template>
  <div class="max-w-sm mx-auto p-6 bg-white rounded-lg shadow-lg">
    <h2 class="text-2xl font-bold text-center mb-6">Login</h2>
    <form @submit.prevent="login" class="space-y-4">
      <div>
        <label for="username" class="block text-gray-700 font-medium"
          >Username</label
        >
        <input
          v-model="username"
          type="text"
          id="username"
          required
          class="w-full p-3 mt-1 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>
      <div>
        <label for="password" class="block text-gray-700 font-medium"
          >Password</label
        >
        <input
          v-model="password"
          type="password"
          id="password"
          required
          class="w-full p-3 mt-1 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>
      <button
        type="submit"
        class="w-full py-3 mt-4 bg-blue-500 text-white font-semibold rounded-md hover:bg-blue-600 transition duration-200"
      >
        Login
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

const username = ref("");
const password = ref("");
const router = useRouter();

const login = async () => {
  try {
    // Отправляем запрос на авторизацию
    const response = await axios.post("http://127.0.0.1:8000/auth/token/", {
      username: username.value,
      password: password.value,
    });

    console.log(response.data);
    // Сохраняем токен в localStorage
    localStorage.setItem("access_token", response.data.access);
    localStorage.setItem("username", username.value);

    // Перенаправляем на главную страницу после успешного входа
    router.push("/Profile");
  } catch (error) {
    console.error("Login failed:", error);
  }
};
</script>
