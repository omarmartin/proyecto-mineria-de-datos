import { createApp } from 'vue'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import router from './routers.js'

const app = createApp(App)
//app.use(vuetify)
app.use(router)

app.mount('#app')
