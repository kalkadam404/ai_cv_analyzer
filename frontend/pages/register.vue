<template>
  <div class="max-w-md mx-auto mt-10 p-6 bg-white shadow-md rounded">
    <h1 class="text-2xl font-bold mb-4">Register</h1>

    <form @submit.prevent="register">
      <div class="mb-4">
        <label class="block mb-1">Username</label>
        <input
          v-model="username"
          type="text"
          class="border p-2 w-full rounded"
          required
        />
      </div>

      <div class="mb-4">
        <label class="block mb-1">Email</label>
        <input
          v-model="email"
          type="email"
          class="border p-2 w-full rounded"
          required
        />
      </div>

      <div class="mb-4">
        <label class="block mb-1">Password</label>
        <input
          v-model="password"
          type="password"
          class="border p-2 w-full rounded"
          required
        />
      </div>

      <div class="mb-4">
        <label class="block mb-1">Role</label>
        <select v-model="role" class="border p-2 w-full rounded">
          <option value="job_seeker">Job Seeker</option>
          <option value="recruiter">Recruiter</option>
        </select>
      </div>

      <button
        type="submit"
        class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        Register
      </button>
    </form>

    <p v-if="error" class="text-red-500 mt-4">{{ error }}</p>
    <p v-if="success" class="text-green-500 mt-4">
      Registration successful! 🎉
    </p>
  </div>
</template>

<script setup>
import { ref } from "vue";

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
    await $fetch("http://127.0.0.1:8000/auth/register/", {
      method: "POST",
      body: {
        username: username.value,
        email: email.value,
        password: password.value,
        role: role.value,
      },
    });
    success.value = true;
  } catch (err) {
    error.value =
      err?.data?.email?.[0] ||
      err?.data?.username?.[0] ||
      "Registration failed";
  }
};
</script>
