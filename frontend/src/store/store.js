import { reactive } from "vue";
import axios from 'axios'

const store = reactive({
    //Usado en Análisis_correlacional.vue
    urls: {
        image_url : '../src/assets/imagen.jpg',
        ruta: './image/correlacion_pearson.png',
    },
    //Usado en Regresión logística
    formdata: {
        id: '',
        radius: '',
        texture: '',
        perimeter: '',
        area: '',
        smoothness: '',
        compactness: '',
        concavity: '',
        concave_points: '',
        symmetry: '',
        fractal_dimension: '',
        reglas: ''
      },
      //Usado en Reglas_de_asociacion
      reglas_asociacion: {
        support: '',
        confidence: '',
        lift: '',
        reglas: ''
      },
      //Usado en clust_particional
      clustering: {
        agruparPor: '',
        encabezados: "",
        checkboxes: [],
        value: [],
        val: [], 
        label: [],
        imagen: './image/evaluacionvisual.png'
      },

      //Usado en Reglas_de_asociacion
      enviar(){
        const requestOptions = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(this.formdata)
        };
        fetch('http://127.0.0.1:5000/reglas_asociacion', requestOptions)
        .then(res => res.json())
        .then(data => {
          this.formdata.reglas = data
          console.log(this.formdata.reglas)
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

      //Usado en Regresión logística
      enviar_datos(){
        
        const requestOptions = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(this.formdata)
        };
        fetch('http://127.0.0.1:5000/regresion', requestOptions)
        .then(res => res.json())
        .then(data => {
          this.formdata.reglas = data
          console.log(this.formdata.reglas)
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
    
    //Usado en Analisis_correlacional.vue
    makeGetRequest(parametro) {
        console.log(parametro)
        let res = axios.get('http://127.0.0.1:5000/correlaciones');
  
        let data = res.data;
        console.log(data);
    },

    //Usado en clust_particional
    enviarGroupBy(){
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(this.clustering)
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
    //Usado en clust_particional
    enviarCorrelacion(){
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(this.clustering)
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
    //Usado en clust_particional
    get_headers2(){
      axios.get('http://127.0.0.1:5000/datos_headers', {
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then(response => {
          //this.headers = response.data
          this.encabezados = response.data
          console.log(this.clustering.encabezados.columns)
      })
    },
    //Usado en clust_particional
    enviaVar() {
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
    //Usado en clust_particional
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
    },

});

export default store