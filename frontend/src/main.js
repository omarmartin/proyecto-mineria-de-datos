import { createApp } from 'vue'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import router from './routers.js'
//import VueJsonToTable from 'vue-json-to-table'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

const app = createApp(App)
app.use(Vuetify)
app.use(router)
app.mount('#app')