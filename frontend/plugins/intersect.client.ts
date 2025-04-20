// import { useIntersectionObserver } from "@vueuse/core";

// export default defineNuxtPlugin((nuxtApp) => {
//   nuxtApp.vueApp.directive("intersect", {
//     mounted(el, binding) {
//       const { stop } = useIntersectionObserver(
//         el,
//         ([{ isIntersecting }]) => {
//           if (isIntersecting) {
//             binding.value?.();
//           }
//         },
//         {
//           threshold: 0.1,
//         }
//       );
//       el._stopObserver = stop;
//     },
//     unmounted(el) {
//       el._stopObserver?.();
//     },
//   });
// });
