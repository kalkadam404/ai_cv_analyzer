<template>
  <section class="border-t border-slate-300">
    <div
      class="px-20 flex flex-col items-center gap-2 mt-20 mb-20"
      data-aos="fade-up"
    >
      <div class="font-bold text-4xl">Поиск вакансий</div>
      <p class="text-slate-500 text-xl font-medium">
        Найдите подходящую вакансию с помощью нашего умного поиска
      </p>
      <div class="flex items-center gap-3 mt-5">
        <input
          type="text"
          placeholder="Должность, навыки или компания"
          class="py-2 px-4 border border-slate-300 rounded-[6px] w-[400px]"
        />
        <button
          class="flex items-center gap-2 text-white bg-black font-medium rounded-[6px] text-center px-5 py-2"
        >
          <img src="../assets/search_icon1.svg" alt="" class="w-5 h-5" />
          Поиск
        </button>
      </div>
      <div class="flex items-center gap-3 mt-5">
        <button
          class="border border-slate-400 hover:bg-gray-300 rounded-[6px] px-5 py-2 transition duration-300"
        >
          IT и разработка
        </button>
        <button
          class="border border-slate-400 hover:bg-gray-300 rounded-[6px] px-5 py-2 transition duration-300"
        >
          Маркетинг
        </button>
        <button
          class="border border-slate-400 hover:bg-gray-300 rounded-[6px] px-5 py-2 transition duration-300"
        >
          Финансы
        </button>
        <button
          class="border border-slate-400 hover:bg-gray-300 rounded-[6px] px-5 py-2 transition duration-300"
        >
          Продажи
        </button>
        <button
          class="border border-slate-400 hover:bg-gray-300 rounded-[6px] px-5 py-2 transition duration-300"
        >
          Дизайн
        </button>
      </div>
      <div class="flex gap-5 mt-10 justify-between">
        <JobCard />
        <JobCard />
        <JobCard />
      </div>
      <button
        class="mt-6 flex items-center gap-2 border border-slate-400 hover:bg-gray-300 rounded-[6px] px-5 py-2 transition duration-300"
      >
        Показать больше вакансий
        <img src="../assets/right_black.svg" alt="" />
      </button>
    </div>
  </section>
</template>
