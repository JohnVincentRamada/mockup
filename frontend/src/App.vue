<script setup>
import { RouterLink, RouterView } from 'vue-router'
import store from '@/store'
</script>

<template>
  <div id="wrapper">
    <nav class="navbar sticky-top navbar-expand-lg px-5 mb-4">
      <div class="container-fluid" v-if="store.state.isAuthenticated">
        <div class="collapse navbar-collapse">
          <ul class="navbar-nav">
            <li class="nav-item">
              <RouterLink class="nav-link fw-bold" to="/">Home</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link fw-bold" to="/account">Account</RouterLink>
            </li>
          </ul>
        </div>
        <button class="btn btn-outline-success my-2"  @click="logout">Logout</button>
        
      </div>

      <div class="container-fluid" v-else>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav my-2">
            <li class="nav-item">
              <RouterLink to="/login" class="nav-link fw-bold">Login</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink to="/register" class="nav-link fw-bold">Register</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>




    
  </div>
  <RouterView />
  
</template>
<script>
import axios from 'axios'
import store from '@/store'

export default {
  
  beforeCreate() {
    

    const token = store.state.token

    if (token) {
        axios.defaults.headers.common['Authorization'] = "Bearer " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted() {
    setInterval(()=>{
      this.getAccess()
    }, 60000);
  },
  methods: {
    logout(){
      localStorage.removeItem("token")
      localStorage.removeItem("refreshToken")
      localStorage.removeItem("username")
      localStorage.removeItem("userid")

      store.dispatch('Logout');
      this.$router.push('/login')
    },
    getAccess(e){
      const AccessData = {
        refresh: store.state.refreshToken
      }
      axios
      .post('api/token/refresh/', AccessData)
      .then(response =>{
        const token = response.data.access
        console.log(token)
        
        store.commit('setToken', { token, refreshToken: store.state.refreshToken });
      })
      .catch(error =>{
        console.log(error)
      })
    }
  }

}

</script>

<style>
@import '../node_modules/bootstrap';
</style>
