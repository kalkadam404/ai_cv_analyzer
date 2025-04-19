import { defineStore } from "pinia";
import jwtDecode from "jwt-decode";

export const useUserStore = defineStore("user", {
  state: () => ({
    access: null,
    refresh: null,
    userInfo: null,
  }),
  persist: true,
  actions: {
    setTokens(access, refresh) {
      this.access = access;
      this.refresh = refresh;
      this.userInfo = jwtDecode(access);
    },
    logout() {
      this.access = null;
      this.refresh = null;
      this.userInfo = null;
    },
  },
});
