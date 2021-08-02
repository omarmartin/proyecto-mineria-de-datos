<template>
   <nav class="navbar navbar-expand-lg bg-light">
    <router-link class="navbar-brand text-style" to="/"> Flask and vue3 </router-link>

  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav ms-auto">
      <li class="nav-item mx-2">
        <router-link class="btn btn-primary" to="/">Home</router-link>
      </li>
      <li class="nav-item">
        <router-link class="btn btn-success" to="/create">Create</router-link>
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
.text-style{
    font-size: 30px !important;
    color:green !important;
    font-family: fantasy !important;
    }
</style>