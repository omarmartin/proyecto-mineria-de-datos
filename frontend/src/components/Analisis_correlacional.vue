<template>
  <div class="heatmap">
    <h1>Esta es la página de analisis correlacional</h1>
    <h2>Mapa de calor</h2>
    <img class="heatmap" src='/image/correlacion_pearson.png'>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data(){
    return {
      image_url : "../src/assets/imagen.jpg",
      ruta: "/image/correlacion_pearson.jpg"
    }
  },
  methods: {
      async makeGetRequest() {

      let res = await axios.get('http://127.0.0.1:5000/correlaciones');

      let data = res.data;
      console.log(data);
      },
    },

  mounted() {
    this.makeGetRequest()
    this.ruta = ''
    this.ruta = 'hola'
  },
  updated() {
    this.makeGetRequest
  },
}
</script>

<style>
.heatmap{
  text-align: center;
}
</style>