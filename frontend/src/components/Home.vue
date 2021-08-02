<template>
 <div class="container mt-5">
   <div v-for="article in articles" :key= "article.id">
     <h3>{{article.id}}  <h2>{{article.nombre}}</h2></h3>
    
   </div>
 </div>
</template>

<script>
export default {

  data(){
    return {
      articles: []
    }
  },



  methods: {
    get_articles(){
      fetch('http://127.0.0.1:5000/get', {
        method: "GET",
        headers: {
          "Content-Type": "application/json"
        }
      })
      .then(res => res.json())
      .then(data => {
        console.log(data)
        this.articles.push(...data)
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

  created(){
    this.get_articles()
  }
}
</script>

<style>

</style>