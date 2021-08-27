<template>
  <div class="container">
    <div class="grid">
      <div>
        <!-- apriori form ===================== -->
        <div class="agrupacion-form">
          <form id="agrupacion-form" @submit.prevent="store.enviarGroupBy" method="POST">
            <!-- support -->
            <div class="field-support">
            <label class="label">Agrupar por</label>
              <input type="text" class="input_text" name="agruparPor" v-model="store.clustering.agruparPor">
            </div>
            <!-- submit button -->
            <div class="field has-text-right">
              <button class="button is-danger">Submit</button>
            </div>
          </form>
        </div>
        <div class="heatmap-form">
        <form id="heatmap-form" @submit.prevent="store.enviarCorrelacion" method="POST">
          <!-- support -->
          <div class="field-support">
            <label class="label">Mostrar correlacion</label>
          </div>
          <!-- submit button -->
          <div class="field has-text-right">
            <button class="button is-danger">Submit</button>
          </div>
        </form>
      </div>
       <div class="variables">
        <!--<label v-for="(variables,index) in agrupacion.encabezados.columns" :key="index"><input type="radio" v-model="showFirst" value="true" />{{variable}}</label
        ><br /> -->          
          <form id="variables-form" @submit.prevent="store.enviaVar" method="POST"  >
            <div class="field has-text-right" v-for="(header, index) in store.clustering.encabezados.columns" :key="index">
               <input type="checkbox" :id="store.clustering.header" :value="store.clustering.header" v-model="store.clustering.checkboxes" />
                <label for="{{header}}">__{{header}}</label>
            </div>
            <span>Checked names: {{ store.clustering.checkboxes }}</span>
            <div>
              <button class="button is-danger">Submit</button>
            </div>
          </form>
      </div>
      <div class="cluster-form">
        <form id="heatmap-form" @submit.prevent="store.clasificar_clusters" method="POST">
          <!-- support -->
          <div class="field-support">
            <label class="label">Clasificar clusters</label>
          </div>
          <!-- submit button -->
          <div class="field has-text-right">
            <button class="button is-danger">Submit</button>
          </div>
        </form>
      </div>
      </div>

      <div class="evaluacion_visual" >
          <img class="image" :src="store.clustering.imagen">
      </div>
      
    </div>
  </div>
</template>

<script>
import store from '../store/store'
export default {
  setup(){
    return{
    store
    }
  },

  computed: {
    checked: {
      get () {
        console.log(store.clustering.value)
        return store.clustering.value
      },
      set (val) {
        this.store.clustering.checkedProxy = val
      }
    }
  },
  mounted() {
    store.get_headers2()
  },
}
</script>

<style>

.grid{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(4, 1fr); 
  width: 100%;
}

.grid .agrupacion-form{
  align-self: top;
  text-align: left;
  margin-left: 100px;
  grid-column: 1;
  grid-row: 1;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

.agrupacion-form .button{
  font-size: 1rem;
}

.input_text{
  background-color:burlywood;
  margin-right: 100px;
}

.grid .heatmap-form{
  align-self: top;
  margin-left: 100px;
  grid-column: 1;
  grid-row: 2;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

.heatmap-form .button{
  font-size: 1rem;
}

.grid .variables{
  text-align: left;
  margin-left: 100px;
  grid-column: 1;
  grid-row: 3;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

.variables .button{
  font-size: 1rem;
}

.grid .cluster-form{
  text-align: left;
  margin-left: 100px;
  grid-column: 1;
  grid-row: 4;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

.cluster-form .button{
  font-size: 1rem;
}

.grid .evaluacion_visual{
    grid-column: 2;
    grid-row: span;
}

.evaluacion_visual img{
  width: 750px;
  height: 750px;
  text-align: left;
}
</style>