<template>
  <div id="app">
    
    <Navbar/>
    <div class="container">
      <router-view/>
    </div>
    <Footer/>
  </div>
</template>

<script>
import Footer from './components/Footer.vue'
import Navbar from './components/Navbar.vue'
export default {
  name: 'App',

  components: {
    Navbar,
    Footer,
  },

  data: () => ({
    //
  }),
}
</script>

<style>
#app{
  background-color:#55423d;
  height: 1080px;
}
p, label, span{
  color: #fff3ec;
}
</style>
