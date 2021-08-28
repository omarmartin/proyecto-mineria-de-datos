<template>
  <div class="container">
    <div class="heatmap">
      <h2>Mapa de calor</h2>
      <img class="heatmap" :src='store.urls.ruta'>
      <p>{{store.makeGetRequest("hola")}}</p>
    </div>
  </div>
</template>




<script>
import store from '../store/store'

export default {
  setup(){
    return {
      store
    }
  },
  mounted(){
    console.log(store.ruta)
  }
}
</script>

<style>
.heatmap{
  text-align: center;
}
h2{
  color: #fffffe;
}
</style>