<template>
  <div
    class="relative bg-white w-[600px] shadow-xl flex flex-col items-start rounded-lg gap-5 py-9 px-10 m-auto"
  >
    <img
      src="../assets/close.svg"
      class="absolute top-4 right-4 w-8 h-8 cursor-pointer"
      alt=""
      @click="$emit('closeRegisterModal')"
    />
    <div>
      <div class="text-2xl font-bold">Создание аккаунта</div>
      <p class="text-gray-500">Заполните форму ниже, чтобы создать аккаунт</p>
    </div>
    <form @submit.prevent="register" class="w-full flex flex-col gap-4">
      <div>
        <label for="username" class="block text-gray-700 font-medium"
          >Имя пользователя</label
        >
        <input
          v-model="username"
          type="text"
          id="username"
          required
          placeholder="Придумайте имя пользователя"
          class="w-full p-3 mt-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-black"
        />
      </div>
      <div>
        <label for="email" class="block text-gray-700 font-medium">Email</label>
        <input
          v-model="email"
          type="text"
          required
          placeholder="Введите ваш email"
          class="w-full p-3 mt-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-black"
        />
      </div>
      <div>
        <label for="username" class="block text-gray-700 font-medium"
          >Тип пользователя</label
        >
        <select v-model="role" class="border p-2 w-full rounded">
          <option value="job_seeker">Соискатель</option>
          <option value="recruiter">Работодатель</option>
        </select>
      </div>

      <div>
        <div class="flex justify-between items-center">
          <label for="password" class="block text-gray-700 font-medium"
            >Пароль</label
          >
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
        </div>
      </div>

      <div class="flex items-center mt-1">
        <input
          type="checkbox"
          id="rememberMe"
          class="w-4 h-4 text-black border-gray-300 rounded focus:ring-black"
        />
        <label for="rememberMe" class="ml-2 text-gray-700"
          >Я согласен с условиями использования и политикой
          конфиденциальности</label
        >
      </div>
      <button
        type="submit"
        class="w-full py-3 mt-1 bg-black text-white font-semibold rounded-md hover:bg-gray-500 transition duration-200"
      >
        Зарегистрироваться
      </button>
    </form>
    <div class="flex items-center justify-center mt-1 mx-auto">
      <span class="text-gray-500">Уже есть аккаунт?</span>
      <span
        @click="$emit('openLoginModal')"
        class="ml-2 text-black font-semibold cursor-pointer"
        >Войти</span
      >
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const userStore = useUserStore();
const emit = defineEmits([
  "closeRegisterModal",
  "toggleToRegister",
  "openLoginModal",
]);

const username = ref("");
const email = ref("");
const password = ref("");
const role = ref("job_seeker");
const error = ref(null);
const success = ref(false);

const register = async () => {
  error.value = null;
  success.value = false;

  try {
    await userStore.register(
      username.value,
      email.value,
      password.value,
      role.value
    );
    success.value = true;
  } catch (err) {
    console.error("Registration error:", err);
    error.value =
      err?.username?.[0] ||
      err?.email?.[0] ||
      err?.password?.[0] ||
      err?.role?.[0] ||
      "Ошибка регистрации";
  }
  emit("closeRegisterModal");
  emit("openLoginModal"); // открываем модалку входа
};
</script>
