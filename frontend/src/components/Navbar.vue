<template>
   <nav class="navbar navbar-expand-lg">
    <router-link class="navbar-brand text-style" to="/"> Mineria de datos </router-link>

  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav ms-auto">
      <li class="nav-item">
        <router-link class="btn btn-primary" to="/">Home</router-link>
      </li>
      <li class="nav-item">
        <router-link class="btn btn-primary" to="/datos">Datos</router-link>
      </li>
      <li class="nav-item">
        <router-link class="btn btn-primary" to="/reglas_asociacion">Reglas de asociación</router-link>
      </li>
      <li class="nav-item">
        <router-link class="btn btn-primary" to="/analisis_correlacional">Analisis correlacional</router-link>
      </li>
      <li class="nav-item">
        <router-link class="btn btn-primary" to="/clustering_particional">Clustering</router-link>
      </li>
      <li class="nav-item">
        <router-link class="btn btn-primary" to="/regresion_logistica">Regresión logística</router-link>
      </li>
    </ul>
  </div>
</nav>
   
</template>

<script>
export default {

}
</script>

<style>
.navbar-brand{
  color: aquamarine;
}
.btn{
  width: 195px;
  font-size: 18px !important;
  font-family: fantasy !important;
  margin-left: 10px;
  margin-right: 10px;
}
.text-style{
    font-size: 30px !important;
    color: ghostwhite !important;
    font-family: fantasy !important;
    margin-left: 10px;
    }

.navbar{
  background-color:darkcyan;
}
</style>