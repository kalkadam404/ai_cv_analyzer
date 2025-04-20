<script setup>
const isLoginModalVisible = ref(false);
const isRegisterModalVisible = ref(false);

const openLoginModal = () => {
  isLoginModalVisible.value = true;
  isRegisterModalVisible.value = false;
};

const closeLoginModal = () => {
  isLoginModalVisible.value = false;
  isRegisterModalVisible.value = false;
};
const toggleToRegister = () => {
  isLoginModalVisible.value = false;
  isRegisterModalVisible.value = true;
};
</script>

<template>
  <div>
    <Header
      @openLoginModal="openLoginModal"
      @toggleToRegister="toggleToRegister"
    />
    <NuxtPage />
    <Footer />

    <transition name="fade">
      <div
        v-if="isLoginModalVisible"
        class="fixed inset-0 z-50 flex items-center justify-center"
      >
        <div
          class="absolute inset-0 bg-black/40 backdrop-blur-md backdrop-saturate-150 transition-all duration-300 ease-in-out z-40"
          @click="closeLoginModal"
        ></div>

        <transition name="scale-fade">
          <div class="relative z-50">
            <Login
              @closeLoginModal="closeLoginModal"
              @toggleToRegister="toggleToRegister"
            />
          </div>
        </transition>
      </div>
    </transition>

    <transition name="fade">
      <div
        v-if="isRegisterModalVisible"
        class="fixed inset-0 z-50 flex items-center justify-center"
      >
        <div
          class="absolute inset-0 bg-black/40 backdrop-blur-md backdrop-saturate-150 transition-all duration-300 ease-in-out z-40"
          @click="closeLoginModal"
        ></div>

        <transition name="scale-fade">
          <div class="relative z-50">
            <Register
              @closeRegisterModal="closeLoginModal"
              @openLoginModal="openLoginModal"
            />
          </div>
        </transition>
      </div>
    </transition>
  </div>
</template>

<style scoped>
/* затемнение */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
.fade-enter-to,
.fade-leave-from {
  opacity: 1;
}

/* анимация появления модалки */
.scale-fade-enter-active,
.scale-fade-leave-active {
  transition: all 0.3s ease;
}
.scale-fade-enter-from,
.scale-fade-leave-to {
  opacity: 0;
  transform: scale(0.9);
}
.scale-fade-enter-to,
.scale-fade-leave-from {
  opacity: 1;
  transform: scale(1);
}
</style>
