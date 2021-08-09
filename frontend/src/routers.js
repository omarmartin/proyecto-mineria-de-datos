import {createRouter, createWebHistory} from 'vue-router'
import Home from './components/Home'
import Analisis_correlacional from './components/Analisis_correlacional'
import Clust_particional from './components/Clust_particional'
import Datos from './components/Datos'
import Reglas_de_asociacion from './components/Reglas_de_asociacion'
import Regresion_logistica from './components/Regresion_logistica'

const routes = [
    {
        path: '/',
        name: 'home',
        component:Home
    },
    {
        path: '/Datos',
        name: 'datos',
        component:Datos
    },
    {
        path: '/Reglas_asociacion',
        name: 'reglas',
        component:Reglas_de_asociacion
    },
    {
        path: '/Analisis_correlacional',
        name: 'analisis',
        component:Analisis_correlacional
    },
    {
        path: '/Clustering_particional',
        name: 'clust_part',
        component:Clust_particional
    },
    {
        path: '/Regresion_logistica',
        name: 'regresion',
        component:Regresion_logistica
    }
    
]

const router = createRouter({
    history:createWebHistory(),
    routes,
})

export default router;