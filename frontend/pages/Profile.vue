<template>
  <div class="bg-gray-100 min-h-screen">
    <!-- Profile Content -->
    <div class="py-10">
      <div class="max-w-4xl mx-auto bg-white p-8 rounded-lg shadow-lg">
        <h1 class="text-3xl font-bold text-center mb-6">Your Profile</h1>
        <p class="text-center text-gray-600 mb-8">
          Welcome to your profile! Here you can view and manage your uploaded
          resumes.
        </p>

        <!-- Компонент для отображения списка резюме -->
        <ListResumes />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
import { onMounted } from "vue";
import ListResumes from "../components/ListResumes.vue";

const router = useRouter();

onMounted(() => {
  // Проверяем, есть ли токен в localStorage только на клиенте
  if (typeof window !== "undefined" && !localStorage.getItem("access_token")) {
    router.push("/login");
  }
});
</script>

<style scoped>
h1 {
  color: #333;
}
</style>
