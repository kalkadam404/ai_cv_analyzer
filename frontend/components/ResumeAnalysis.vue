<template>
  <section class="flex items-center gap-3 px-20 bg-[#F9F9F9] pt-30 pb-30">
    <div class="flex flex-col gap-8" data-aos="fade-right">
      <div
        class="flex items-center gap-2 rounded-xl py-1 px-3 mt-5 bg-gray-100 w-max"
      >
        <img src="../assets/blank.svg" class="w-4 h-4" alt="" />
        Анализ резюме
      </div>
      <div class="font-bold text-5xl">Улучшите своё резюме с помощью ИИ</div>
      <p class="text-gray-400 text-xl font-medium w-[650px]">
        Наш умный анализатор резюме поможет вам выделиться среди других
        кандидатов и повысить шансы на получение работы мечты.
      </p>
      <div class="flex flex-col gap-5">
        <div class="flex items-center gap-3">
          <img src="../assets/selected.svg" alt="" />
          Анализ ключевых навыков и компетенций
        </div>
        <div class="flex items-center gap-3">
          <img src="../assets/selected.svg" alt="" />
          Рекомендации по улучшению структуры и содержания
        </div>
        <div class="flex items-center gap-3">
          <img src="../assets/selected.svg" alt="" />
          Сравнение с требованиями вакансий
        </div>
        <div class="flex items-center gap-3">
          <img src="../assets/selected.svg" alt="" />
          Проверка грамматики и стиля
        </div>
      </div>
    </div>
    <div
      class="flex flex-col gap-3 bg-white w-[1100px] rounded-xl shadow-lg p-8"
      data-aos="fade-left"
    >
      <div
        class="flex flex-col items-center justify-center gap-3 h-[300px] border-2 border-dashed border-gray-200 rounded-xl py-2"
      >
        <img
          src="../assets/upload.svg"
          alt=""
          class="w-12 h-12 p-2.5 rounded-full bg-gray-100"
        />
        <div class="text-lg">Загрузите своё резюме</div>
        <p class="text-base text-gray-500 font-mono">
          Поддерживаемые форматы: PDF, DOCX, TXT
        </p>
        <button
          class="bg-black text-white py-1.5 px-4 rounded-[6px] font-medium"
        >
          Выбрать файл
        </button>
      </div>
      <div class="text-xl mt-3">Результаты анализа</div>
      <div
        class="flex items-center justify-between bg-[#F3F3F3] py-6 px-5 rounded-[8px]"
      >
        <div class="flex items-center gap-3 text-xl font-sans">
          <img src="../assets/warning.svg" alt="" />
          Отсутствуют ключевые навыки
        </div>
        <div class="text-lg font-medium">Исправить</div>
      </div>
      <div
        class="flex items-center justify-between bg-[#F3F3F3] py-6 px-5 rounded-[8px]"
      >
        <div class="flex items-center gap-3 text-xl font-sans">
          <img src="../assets/warning.svg" alt="" />
          Улучшите описание опыта работы
        </div>
        <div class="text-lg font-medium">Исправить</div>
      </div>
      <div
        class="flex items-center justify-between bg-[#F3F3F3] py-4 px-5 rounded-[8px]"
      >
        <div class="flex items-center gap-3 text-xl font-sans">
          <img src="../assets/done.svg" alt="" />
          Хорошая структура резюме
        </div>
      </div>
      <button
        class="bg-black text-white py-2 px-4 rounded-[6px] font-medium mt-3"
      >
        Получить полный анализ
      </button>
    </div>
  </section>
</template>
