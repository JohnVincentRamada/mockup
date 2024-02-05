import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import HomeView from '../views/HomeView.vue'
import AccountView from '../views/AccountView.vue'
import RegisterView from '../views/RegisterView.vue'
import CreateResumeView from '../views/CreateResumeView.vue'
import UpdateProfileView from '../views/UpdateProfileView.vue'
import store from '../store'

const router = createRouter({
  
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: { requiresAuth: true }
      
    },
    {
      path: '/updateprofile',
      name: 'updateprofile',
      component: UpdateProfileView,
      meta: { requiresAuth: true }
      
    },
    {
      path: '/createresume',
      name: 'createresume',
      component: CreateResumeView,
      meta: { requiresAuth: true }
      
    },
    {
      path: '/account',
      name: 'account',
      component: AccountView,
      meta: { requiresAuth: true }
      
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    }
  ]
})

router.beforeEach((to, from, next) => {
  const isAuthenticated = store.getters.isAuthenticated;

  if (to.matched.some(record => record.meta.requiresAuth) && !isAuthenticated) {
      
    next({ name: 'login', query: { to: to.path } }); 
  } else {
      next();
  }
})

export default router
