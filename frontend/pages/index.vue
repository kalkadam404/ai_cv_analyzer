<template>
  <div>
    <main class="flex gap-5 justify-between items-center mt-20 mb-20 px-20">
      <div class="flex flex-col gap-4">
        <div class="font-bold text-5xl">
          Найдите идеальную работу и улучшите своё резюме
        </div>
        <div class="text-slate-500 text-xl font-medium mt-2 mb-4">
          Используйте наш умный поиск вакансий и анализ резюме, чтобы выделиться
          среди других кандидатов и найти работу своей мечты.
        </div>
        <div class="flex items-center gap-3">
          <button
            class="flex items-center gap-2 text-white bg-black font-medium rounded-[6px] text-center px-5 py-2"
          >
            Начать поиск
            <img src="../assets/right.svg" alt="" class="w-3 h-3" />
          </button>
          <button class="px-5 py-2 border border-slate-600 rounded-[6px]">
            Анализ резюме
          </button>
        </div>
      </div>
      <div>
        <img src="../assets/search.png" alt="" />
      </div>
    </main>
    <section class="border-t border-slate-300">
      <div class="px-20 flex flex-col items-center gap-2 mt-20 mb-20">
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
    <section class="flex items-center gap-3 px-20 bg-[#F9F9F9] pt-30 pb-30">
      <div class="flex flex-col gap-8">
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
    <section>
      <div class="flex flex-col gap-3 items-center mt-30 mb-30">
        <div class="font-bold text-5xl">Как это работает</div>
        <p class="text-gray-400 text-xl font-medium">
          Простой процесс поиска работы и улучшения резюме в три шага
        </p>

        <div class="flex gap-7 justify-between">
          <div
            class="relative border border-gray-200 w-[400px] mt-10 pt-10 p-5 rounded-xl"
          >
            <img
              src="../assets/search_icon1.svg"
              alt=""
              class="absolute -top-5 left-6 w-12 h-12 p-3 rounded-full bg-black"
            />
            <div class="font-bold text-xl">1. Поиск вакансий</div>
            <p class="text-base text-gray-500 font-normal">
              Используйте наш умный поиск, чтобы найти вакансии, соответствующие
              вашим навыкам и опыту.
            </p>
            <img
              src="../assets/arrow-right.svg"
              alt=""
              class="absolute -right-6 bottom-12"
            />
          </div>
          <div
            class="relative border border-gray-200 w-[400px] mt-10 pt-10 p-5 rounded-xl"
          >
            <img
              src="../assets/blank1.svg"
              alt=""
              class="absolute -top-5 left-6 w-12 h-12 p-3 rounded-full bg-black"
            />
            <div class="font-bold text-xl">2. Анализ резюме</div>
            <p class="text-base text-gray-500 font-normal">
              Загрузите своё резюме для анализа и получите рекомендации по его
              улучшению.
            </p>
            <img
              src="../assets/arrow-right.svg"
              alt=""
              class="absolute -right-6 bottom-12"
            />
          </div>
          <div
            class="relative border border-gray-200 w-[400px] mt-10 pt-10 p-5 rounded-xl"
          >
            <div class="font-bold text-xl">3. Подача заявки</div>
            <p class="text-base text-gray-500 font-normal">
              Отправьте улучшенное резюме и увеличьте свои шансы на получение
              работы мечты.
            </p>
          </div>
        </div>
      </div>
    </section>
    <section class="flex flex-col gap-3 items-center pt-30 pb-30 bg-[#F9F9F9]">
      <div class="font-bold text-5xl">Отзывы наших пользователей</div>
      <p class="text-gray-400 text-xl font-normal text-center w-[600px]">
        Узнайте, что говорят о нас люди, которые уже нашли работу с помощью
        JumysTap
      </p>
      <div class="flex items-center gap-3">
        <div
          class="flex flex-col gap-2 bg-white w-[450px] rounded-xl shadow-lg p-6 mt-10"
        >
          <div class="flex items-center">
            <img src="../assets/star.svg" alt="" />
            <img src="../assets/star.svg" alt="" />
            <img src="../assets/star.svg" alt="" />
            <img src="../assets/star.svg" alt="" />
            <img src="../assets/star.svg" alt="" />
          </div>
          <div class="text-lg text-gray-500 font-sans">
            "Благодаря JumysTap я нашел работу своей мечты всего за две недели!
            Анализ резюме помог мне выделиться среди других кандидатов."
          </div>
          <div class="flex items-center gap-4 mt-5">
            <img
              src="../assets/dauka.jpg"
              alt=""
              class="w-12 h-12 rounded-full"
            />
            <div class="flex flex-col">
              <div class="font-bold">Дармен Дәулет</div>
              <div class="text-gray-500">QA-Тестировщик</div>
            </div>
          </div>
        </div>
        <div
          class="flex flex-col gap-2 bg-white w-[450px] rounded-xl shadow-lg p-6 mt-10"
        >
          <div class="flex items-center">
            <img src="../assets/star.svg" alt="" />
            <img src="../assets/star.svg" alt="" />
            <img src="../assets/star.svg" alt="" />
            <img src="../assets/star.svg" alt="" />
            <img src="../assets/star.svg" alt="" />
          </div>
          <div class="text-lg text-gray-500 font-sans">
            "Умный поиск вакансий JumysTap помог мне найти предложения, которые
            идеально соответствуют моим навыкам и опыту. Очень рекомендую!"
          </div>
          <div class="flex items-center gap-4 mt-5">
            <img
              src="../assets/abu.jpg"
              alt=""
              class="w-12 h-12 rounded-full"
            />
            <div class="flex flex-col">
              <div class="font-bold">Қуатұлы Абуханифа</div>
              <div class="text-gray-500">Fullstack-Разработчик</div>
            </div>
          </div>
        </div>
        <div
          class="flex flex-col gap-2 bg-white w-[450px] rounded-xl shadow-lg p-6 mt-10"
        >
          <div class="flex items-center">
            <img src="../assets/star.svg" alt="" />
            <img src="../assets/star.svg" alt="" />
            <img src="../assets/star.svg" alt="" />
            <img src="../assets/star.svg" alt="" />
            <img src="../assets/star.svg" alt="" />
          </div>
          <div class="text-lg text-gray-500 font-sans">
            "Анализ резюме от JumysTap дал мне ценные рекомендации, которые
            помогли улучшить моё резюме и получить больше откликов от
            работодателей."
          </div>
          <div class="flex items-center gap-4 mt-5">
            <img
              src="../assets/alzhik.jpg"
              alt=""
              class="w-12 h-12 rounded-full"
            />
            <div class="flex flex-col">
              <div class="font-bold">Дарибаев Әлжан</div>
              <div class="text-gray-500">Backend-Разработчик</div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="flex flex-col gap-3 items-center pt-30 pb-30 bg-[#ECECEC]">
      <div class="font-bold text-5xl">
        Начните свой путь к новой карьере сегодня
      </div>
      <p class="text-gray-500 text-xl font-normal text-center w-[600px]">
        Присоединяйтесь к тысячам людей, которые уже нашли работу своей мечты с
        помощью JumysTap
      </p>
      <div class="flex items-center gap-3 mt-4">
        <button
          class="bg-black text-white py-2.5 px-5 rounded-[6px] font-medium"
        >
          Создать аккаунт
        </button>
        <button
          class="bg-white text-black py-2.5 px-5 rounded-[6px] font-medium"
        >
          Узнать больше
        </button>
      </div>
    </section>
  </div>
</template>
