export default defineNuxtPlugin((nuxtApp) => {
  const config = useRuntimeConfig();
  const axios = $fetch.create({
    baseURL: config.public.apiBaseUrl,
  });

  return {
    provide: {
      axios,
    },
  };
});
