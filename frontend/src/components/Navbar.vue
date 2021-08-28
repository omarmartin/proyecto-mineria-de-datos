<template>
   <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
     <div class="collapse navbar-collapse" id="navbarNavDropdown">
       <ul class="navbar-nav">
        <li class="nav-item active">
          <router-link class="navbar-brand" to="/"> Mineria de datos </router-link>
        </li>
        <li class="nav-item active">
          <router-link class="nav-item nav-link" to="/">Home </router-link>
        </li>
        <li class="nav-item active">
          <router-link class="nav-item nav-link" to="/datos">Datos</router-link>
        </li>
        <li class="nav-item active">
          <router-link class="nav-item nav-link" to="/reglas_asociacion">Reglas de asociación</router-link>
        </li>
        <li class="nav-item active">
          <router-link class="nav-item nav-link" to="/analisis_correlacional">Análisis correlacional</router-link>
        </li>
        <li class="nav-item active">
          <router-link class="nav-item nav-link" to="/clustering_particional">Clustering</router-link>
        </li>
        <li class="nav-item active">
          <router-link class="nav-item nav-link" to="/regresion_logistica">Regresión logística</router-link>
        </li>
       </ul>  
          
          
          
          
     </div>
  <!--<div class="collapse navbar-collapse" id="navbarNav">
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
  </div> -->

</nav>
   
</template>

<script>
export default {

}
</script>

<style>




</style>