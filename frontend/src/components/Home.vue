<template>
 <div class="container mt-5">
   <form action="http://127.0.0.1:5000/upload" method="POST" enctype="multipart/form-data">
 <input type="file" name="archivo">
 <input type="submit">
 <p>{{articles[0]}}</p>
</form>
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