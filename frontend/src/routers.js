import {createRouter, createWebHistory} from 'vue-router'
import Home from './components/Home'
import Create from './components/Create'
import Analisis_correlacional from './components/Analisis_correlacional'
import Clust_jerarquico from './components/Clust_jerarquico'
import Clust_particional from './components/Clust_particional'
import Datos from './components/Datos'
import Distancias from './components/Distancias'
import Reglas_de_asociacion from './components/Reglas_de_asociacion'
import Regresion_logistica from './components/Regresion_logistica'

const routes = [
    {
        path: '/',
        name: 'home',
        component:Home
    },
    {
        path: '/Create',
        name: 'create',
        component:Create
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
        path: '/Distancias',
        name: 'distancias',
        component:Distancias
    },
    {
        path: '/Clustering_jerarquico',
        name: 'clust_jerarquico',
        component:Clust_jerarquico
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