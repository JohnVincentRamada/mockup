import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import store from './store'
import { library } from "@fortawesome/fontawesome-svg-core"
import { faCircle, faFileCirclePlus, faPenToSquare, faPhone } from "@fortawesome/free-solid-svg-icons"
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome"

library.add(faPhone, faPenToSquare, faFileCirclePlus)

axios.defaults.baseURL = 'http://127.0.0.1:8000'

const app = createApp(App)

app.component("font-awesome-icon", FontAwesomeIcon)
app.use(router, axios, store)
app.mount('#app')
