<template>
  <div
    class="relative bg-white w-[600px] shadow-xl flex flex-col items-start rounded-lg gap-5 py-9 px-10 m-auto"
  >
    <img
      src="../assets/close.svg"
      class="absolute top-4 right-4 w-8 h-8 cursor-pointer"
      alt=""
      @click="$emit('closeLoginModal')"
    />
    <div>
      <div class="text-2xl font-bold">Вход в аккаунт</div>
      <p class="text-gray-500">
        Введите ваш email и пароль для входа в систему
      </p>
    </div>
    <form @submit.prevent="login" class="w-full flex flex-col gap-4">
      <div>
        <label for="username" class="block text-gray-700 font-medium"
          >Имя пользователя</label
        >
        <input
          v-model="username"
          type="text"
          id="username"
          required
          placeholder="Введите ваш username"
          class="w-full p-3 mt-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-black"
        />
      </div>
      <div>
        <div class="flex justify-between items-center">
          <label for="password" class="block text-gray-700 font-medium"
            >Пароль</label
          >
          <div>Забыли пароль?</div>
        </div>
        <div class="relative mt-2">
          <input
            v-model="password"
            type="password"
            id="password"
            required
            placeholder="Введите ваш пароль"
            class="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-black"
          />
          <img
            src="../assets/eye.svg"
            class="absolute right-3 top-1/2 transform -translate-y-1/2 cursor-pointer"
            alt=""
          />
        </div>
      </div>
      <div class="flex items-center mt-4">
        <input
          type="checkbox"
          id="rememberMe"
          class="w-4 h-4 text-black border-gray-300 rounded focus:ring-black"
        />
        <label for="rememberMe" class="ml-2 text-gray-700"
          >Запомнить меня</label
        >
      </div>
      <button
        @click="emit('closeLoginModal')"
        type="submit"
        class="w-full py-3 mt-4 bg-black text-white font-semibold rounded-md hover:bg-gray-500 transition duration-200"
      >
        Войти
      </button>
    </form>
    <div class="flex items-center justify-center mt-4 mx-auto">
      <span class="text-gray-500">У вас нет аккаунта?</span>
      <span
        class="ml-2 text-black font-semibold cursor-pointer"
        @click="$emit('toggleToRegister')"
        >Зарегистрироваться</span
      >
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";
const emit = defineEmits(["closeLoginModal", "toggleToRegister"]);

const username = ref("");
const password = ref("");

const userStore = useUserStore();

const login = async () => {
  try {
    const response = await axios.post("http://127.0.0.1:8000/auth/token/", {
      username: username.value,
      password: password.value,
    });

    const accessToken = response.data.access;
    userStore.login(username.value, accessToken); // авторизация через store

    emit("closeLoginModal"); // закрываем модалку
  } catch (error) {
    console.error("Login failed:", error.response?.data || error);
    alert("Неверный логин или пароль"); // можно добавить alert
  }
};
</script>
