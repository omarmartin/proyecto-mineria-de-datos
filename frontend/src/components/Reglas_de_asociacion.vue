<template class= "template">
  <div class="template">  
    <div class="box">

      <!-- apriori form ===================== -->
      <form id="apriori-form" @submit.prevent="enviar" method="POST">
        <!-- support -->
        <div class="field-support">
          <label class="label">Support</label>
          <input type="text" class="input" name="support"  v-model="formdata.support">
        </div>

        <!-- confidence -->
        <div class="field-confidence">
          <label class="label">Confidence</label>
          <input type="text" class="input" name="confidence"  v-model="formdata.confidence">
        </div>

        <!-- Lift -->
        <div class="field-lift">
          <label class="label">Lift</label>
          <input type="text" class="input" name="lift" v-model="formdata.lift">
        </div>

        <!-- submit button -->
        <div class="field has-text-right">
          <button class="button is-danger">Submit</button>
        </div>
      </form>
      
    </div>
    <div><p v-for="(item,index) in this.formdata.reglas" :key="index">Regla {{item}}</p></div>
  </div>
</template>

<script>
export default {
  data(){
    return{
      formdata: {
        support: '',
        confidence: '',
        lift: '',
        reglas: ''
      }
    }
  },
  methods : {
    enviar(){
      /*console.log(this.formdata)
      let res = axios.post('http://127.0.0.1:5000/reglas_asociacion', this.formdata)      
      this.formdata.reglas = res.data 
      console.log(this.formdata.reglas)*/

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
    }
  }
}
</script>

<style>
.box{
  text-align: center;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  font-size: 3rem;
}
.template{
  background-color:beige;
}
.input{
  background-color: white;
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
</style>