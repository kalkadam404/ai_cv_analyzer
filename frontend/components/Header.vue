<template>
  <header
    class="bg-black text-white shadow-md py-4 px-6 flex justify-between items-center"
  >
    <div class="flex items-center gap-3">
      <NuxtLink
        to="/"
        class="text-2xl font-bold text-white hover:text-gray-400"
      >
        AI Resume
      </NuxtLink>
    </div>

    <nav class="flex gap-4 items-center">
      <NuxtLink to="/" class="text-gray-300 hover:text-white">Главная</NuxtLink>
      <!-- <NuxtLink to="/about" class="text-gray-300 hover:text-white"
        >О нас</NuxtLink
      > -->
      <NuxtLink
        v-if="isLoggedIn"
        to="/profile"
        class="text-gray-300 hover:text-white"
        >Профиль</NuxtLink
      >

      <div v-if="isLoggedIn" class="flex items-center gap-4">
        <span class="text-sm text-gray-400">👋 {{ username }}</span>
        <button
          @click="logout"
          class="bg-red-600 text-white px-4 py-2 rounded-full hover:bg-red-700 transition"
        >
          Выйти
        </button>
      </div>

      <div v-else class="flex gap-4">
        <NuxtLink
          to="/login"
          class="bg-gray-800 text-white px-4 py-2 rounded-full hover:bg-gray-700 transition"
        >
          Войти
        </NuxtLink>
        <NuxtLink
          to="/register"
          class="bg-white text-black px-4 py-2 rounded-full hover:bg-gray-200 transition"
        >
          Регистрация
        </NuxtLink>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

const isLoggedIn = ref(false);
const username = ref("");
const router = useRouter();

onMounted(() => {
  const token = localStorage.getItem("access_token");
  const storedUsername = localStorage.getItem("username");
  if (token && storedUsername) {
    isLoggedIn.value = true;
    username.value = storedUsername;
  }
});

const logout = () => {
  localStorage.removeItem("access_token");
  localStorage.removeItem("username");
  isLoggedIn.value = false;
  router.push("/login");
};
</script>

<style scoped>
header {
  z-index: 10;
  position: sticky;
  top: 0;
  background-color: black;
}

button,
a {
  transition: all 0.3s ease;
}
</style>
