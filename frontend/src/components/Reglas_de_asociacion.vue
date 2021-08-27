<template class= "template">
  <div class="container">  
    <div class="box">

      <!-- apriori form ===================== -->
      <form id="apriori-form" @submit.prevent="store.enviar" method="POST">
        <!-- support -->
        <div class="field-support">
          <label class="label">Support</label>
          <input type="text" class="input" name="support"  v-model="store.reglas_asociacion.support">
        </div>

        <!-- confidence -->
        <div class="field-confidence">
          <label class="label">Confidence</label>
          <input type="text" class="input" name="confidence"  v-model="store.reglas_asociacion.confidence">
        </div>

        <!-- Lift -->
        <div class="field-lift">
          <label class="label">Lift</label>
          <input type="text" class="input" name="lift" v-model="store.reglas_asociacion.lift">
        </div>

        <!-- submit button -->
        <div class="field has-text-right">
          <button class="button is-danger">Submit</button>
        </div>
      </form>
      
    </div>
    <div class="lista_reglas"><p v-for="(item,index) in store.reglas_asociacion.reglas" :key="index" class="letra">Regla {{index}}: {{item}}</p></div>
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
}
</script>

<style>
.box{
  text-align: center;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  font-size: 3rem;
}
.template{
  background-color:coral;
  height: 1080px;
}
.input{
  background-color: coral;
  margin:20px
}
.button{
  background-color:deepskyblue;
}
.field-confidence label{
  padding-right: 20px;
}
.field-support label{
  padding-right: 100px;
}
.field-lift label{
  padding-right: 200px;
}
.button{
  margin: 20px;
}
.lista_reglas{
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  font-size: 1.5rem;
}

</style>