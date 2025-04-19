<template>
  <footer class="sticky top-0 z-50 w-full backdrop-blur bg-white/80 px-20">
    <div
      class="container mx-auto flex items-center justify-between px-4 md:px-6 py-4"
    >
      <!-- Logo -->
      <div class="flex items-center gap-3">
        <img
          src="../assets/ep_suitcase.svg"
          class="w-6 h-6 md:w-7 md:h-7"
          alt="logo"
        />
        <span class="text-xl font-semibold text-gray-800">JumysTap</span>
      </div>

      <!-- Nav (Desktop) -->
      <nav class="hidden md:flex items-center gap-8 text-gray-700">
        <NuxtLink
          href="#"
          class="hover:text-black transition-all duration-200 text-sm font-medium"
        >
          Условия использования
        </NuxtLink>
        <NuxtLink
          href="#"
          class="hover:text-black transition-all duration-200 text-sm font-medium"
        >
          Политика конфиденциальности
        </NuxtLink>
        <NuxtLink
          href="#"
          class="hover:text-black transition-all duration-200 text-sm font-medium"
        >
          Контакты
        </NuxtLink>
      </nav>
      <div
        class="hover:text-black transition-all duration-200 text-[12px] font-medium text-gray-700"
      >
        © 2025 JumysTap. Все права защищены.
      </div>
    </div>
  </footer>
</template>
