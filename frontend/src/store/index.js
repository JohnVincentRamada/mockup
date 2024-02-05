import { createStore } from 'vuex';
import axios from 'axios';

export default createStore({
  state: {
    token: localStorage.getItem('token') || '',
    refreshToken: localStorage.getItem('refreshToken') || '',
    isAuthenticated: !!localStorage.getItem('token'),
    hasResume: false,
    error: null,
  },
  mutations: {
    setToken(state, { token, refreshToken }) {
      state.token = token;
      state.refreshToken = refreshToken;
      localStorage.setItem('token', token);
      localStorage.setItem('refreshToken', refreshToken);
      state.isAuthenticated = true;
    },
    destroyToken(state) {
      state.token = '';
      state.refreshToken = '';
      localStorage.removeItem('token');
      localStorage.removeItem('refreshToken');
      state.isAuthenticated = false;
    },
    setError(state, error) {
      state.error = error;
    }

  },
  getters: {
    isAuthenticated: (state) => state.isAuthenticated,
    error: (state) => state.error,
  },
  actions: {
    async submitForm({ commit }, credentials) {
      axios.defaults.headers.common['Authorization'] = '';
      try {
        const response = await axios.post('api/token/', credentials);
        
        if (response.data.detail) {
          commit('setError', response.data.detail);
        }else {
          const { access: token, refresh: refreshToken } = response.data;
          console.log(token);
          commit('setToken', { token, refreshToken });
          axios.defaults.headers.common['Authorization'] = 'Bearer ' + token;
        }
        
      } catch (error) {
        commit('setError', error.response.data.detail);
      }
    },
    
    Logout({ commit }) {
      axios.defaults.headers.common['Authorization'] = '';
      commit('destroyToken');
    },
  },
  modules: {},
});
