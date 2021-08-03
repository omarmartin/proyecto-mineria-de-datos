<template>
   <nav class="navbar navbar-expand-lg bg-light">
    <router-link class="navbar-brand text-style" to="/"> Mineria de datos </router-link>

  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav ms-auto">
      <li class="nav-item">
        <router-link class="btn btn-primary" to="/">Home</router-link>
      </li>
      <li class="nav-item">
        <router-link class="btn btn-primary" to="/create">Create</router-link>
      </li>
      <li class="nav-item">
        <router-link class="btn btn-primary" to="/datos">Datos</router-link>
      </li>
      <li class="nav-item">
        <router-link class="btn btn-primary" to="/reglas_asociacion">Reglas_asoc</router-link>
      </li>
      <li class="nav-item">
        <router-link class="btn btn-primary" to="/analisis_correlacional">Analisis_cor</router-link>
      </li>
      <li class="nav-item">
        <router-link class="btn btn-primary" to="/distancias">Distancias</router-link>
      </li>
      <li class="nav-item">
        <router-link class="btn btn-primary" to="/clustering_jerarquico">Clust_jer</router-link>
      </li>
      <li class="nav-item">
        <router-link class="btn btn-primary" to="/clustering_particional">Clust_part</router-link>
      </li>
      <li class="nav-item">
        <router-link class="btn btn-primary" to="/regresion_logistica">Reg_logis</router-link>
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
.btn{
  width: 120px;
  font-size: 20px !important;
  font-family: fantasy !important;
  margin-left: 10px;
  margin-right: 10px;
}
.text-style{
    font-size: 30px !important;
    color:green !important;
    font-family: fantasy !important;
    margin-left: 10px;
    }
</style>