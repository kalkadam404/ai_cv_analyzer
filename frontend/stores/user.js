// stores/user.js
import { defineStore } from "pinia";
import axios from "axios";

export const useUserStore = defineStore("user", () => {
  const isLoggedIn = ref(false);
  const username = ref("");
  const token = ref("");

  const login = (name, accessToken) => {
    isLoggedIn.value = true;
    username.value = name;
    token.value = accessToken;

    localStorage.setItem("username", name);
    localStorage.setItem("access_token", accessToken);
  };

  const logout = () => {
    isLoggedIn.value = false;
    username.value = "";
    token.value = "";
    localStorage.removeItem("username");
    localStorage.removeItem("access_token");
  };

  const register = async (username, email, password, role) => {
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/auth/register/",
        {
          username,
          email,
          password,
          role,
        }
      );
      // console.log("Registration successful:", response.data);
      return response.data;
    } catch (error) {
      if (error.response && error.response.data) {
        console.error("Registration failed:", error.response.data);
        throw error.response.data; // пробросить данные ошибки дальше
      } else {
        console.error("Unknown error:", error);
        throw new Error("Unknown registration error");
      }
    }
  };

  const initialize = () => {
    const savedToken = localStorage.getItem("access_token");
    const savedUsername = localStorage.getItem("username");

    if (savedToken && savedUsername) {
      isLoggedIn.value = true;
      username.value = savedUsername;
      token.value = savedToken;
    }
  };

  return {
    isLoggedIn,
    username,
    token,
    login,
    register,
    logout,
    initialize,
  };
});
