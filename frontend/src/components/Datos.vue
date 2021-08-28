<template>
  <div class="container">
    <div class="datos">
        <h3 class="p-3 text-center">Tabla de datos</h3>
        <table class="table table-striped table-bordered">
            <thead>
                <tr>
                    <th v-for="(header, index) in headers.columns" :key="index">
                      {{header}}
                      </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(datos, indexy) in headers.data" :key="indexy">
                    <td  v-for="(dato, index) in datos" :key="index">
                      {{dato}}
                    </td>
                </tr>
            </tbody>
        </table>
      </div>
    </div>    
</template>

<script>
import axios from 'axios'

export default {
  data(){
    return {
      headers : "",
      encabezados: [],
      datos: []
    }
  },

  methods: {

    /*create_list_headers(){
      for(let i=0; i< length(this.headers.columns); i++){
        this.encabezados[i] = this.headers.columns[i]
      }
      for(let i=0; i< length(this.headers.data); i++){
        this.datos[i] = this.headers.data[i]
      }
    },*/

    get_headers(){
      axios.get('http://127.0.0.1:5000/datos_headers', {
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then(response => {
          //this.headers = response.data
          this.headers = response.data
          console.log(this.headers.columns)
          
      })
    },
  },


    /*get_table(){
      axios.get('http://127.0.0.1:5000/datos_table')
      .then(response => {
          this.items = response.data;
          if (response.length > 0){ 
              var columnsIn = res[0]; 
              for(var key in columnsIn){
                console.log(key); // here is your column name you are looking for
              } 
            }else{
                console.log("No columns");
            }
          console.log(response.headers)
      })
    }
  },
  */

  mounted() {
    this.get_headers()
    //this.get_table()
    //this.create_list_headers()
  },
}
</script>

<style>
.container{
  background-color: #55423d;
}
h3{
  color: #fffffe;
}
</style>