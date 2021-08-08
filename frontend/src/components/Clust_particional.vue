<template>
  <div>
    <div class="grid">
      <div>
        <!-- apriori form ===================== -->
        <div class="agrupacion-form">
          <form id="agrupacion-form" @submit.prevent="enviarGroupBy" method="POST">
            <!-- support -->
            <div class="field-support">
            <label class="label">Agrupar por</label>
              <input type="text" class="input_text" name="agruparPor"  v-model="agrupacion.agruparPor">
            </div>
            <!-- submit button -->
            <div class="field has-text-right">
              <button class="button is-danger">Submit</button>
            </div>
          </form>
        </div>
        <div class="heatmap-form">
        <form id="heatmap-form" @submit.prevent="enviarCorrelacion" method="POST">
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
          <form id="variables-form" @submit.prevent="enviaVariables" method="POST"  >
            <div class="field has-text-right" v-for="(header, index) in this.encabezados.columns" :key="index">
               <input type="checkbox" :id="header" :value="header" v-model="checkboxes" />
                <label for="{{header}}">__{{header}}</label>
            </div>
            <span>Checked names: {{ checkboxes }}</span>
            <div>
              <button class="button is-danger">Submit</button>
            </div>
          </form>
      </div>
      <div class="cluster-form">
        <form id="heatmap-form" @submit.prevent="clasificar_clusters" method="POST">
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
          <img class="image" :src="imagen">
      </div>
      
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data(){
    return{
      agrupacion: {
        agruparPor: '',
      },
      encabezados: "",
      checkboxes: [],
      value: [],
      val: [], 
      label: [],
      imagen: './image/evaluacionvisual.png'
    }
  },

  computed: {
    checked: {
      get () {
        console.log(this.value)
        return this.value
      },
      set (val) {
        this.checkedProxy = val
      }
    }
  },

  methods : {

    onChange(){
      if(this.checkedProxy == "true"){
        console.log(this.value)
      }
    },


    enviarGroupBy(){
      console.log(this.agrupacion)
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(this.agrupacion)
      };
      fetch('http://127.0.0.1:5000/clustering_agrupacion', requestOptions)
      .then(res => res.json())
      .then(data => {
        console.log(data)
      })
      .catch(error => {
        if (!error.response) {
            // network error
            this.errorStatus = 'Error: Network Error';
        } else {
            this.errorStatus = error.response.data.message;
        }
      })
    },

    enviarCorrelacion(){
      console.log(this.agrupacion)
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(this.agrupacion)
      };
      fetch('http://127.0.0.1:5000/clustering_correlacion', requestOptions)
      .then(res => res.json())
      .then(data => {
        console.log(data)
      })
      .catch(error => {
        if (!error.response) {
            // network error
            this.errorStatus = 'Error: Network Error';
        } else {
            this.errorStatus = error.response.data.message;
        }
      })
    },

    get_headers2(){
      axios.get('http://127.0.0.1:5000/datos_headers', {
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then(response => {
          //this.headers = response.data
          this.encabezados = response.data
          console.log(this.encabezados.columns)
          
      })
    },
    

    enviaVariables() {
      console.log(this.checkboxes)
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(this.checkboxes)
      };
      fetch('http://127.0.0.1:5000/enviaVariables', requestOptions)
      .then(res => res.json())
      .then(data => {
        console.log(data)
      })
      .catch(error => {
        if (!error.response) {
            // network error
            this.errorStatus = 'Error: Network Error';
        } else {
            this.errorStatus = error.response.data.message;
        }
      })
    },

    clasificar_clusters(){
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(this.checkboxes)
      };
      fetch('http://127.0.0.1:5000/clasificar_clusters', requestOptions)
      .then(res => res.json())
      .then(data => {
        console.log(data)
      })
      .catch(error => {
        if (!error.response) {
            // network error
            this.errorStatus = 'Error: Network Error';
        } else {
            this.errorStatus = error.response.data.message;
        }
      })
    }
  },

  mounted() {
    this.get_headers2()
  },
}
</script>

<style>

.grid{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(4, 1fr); 
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