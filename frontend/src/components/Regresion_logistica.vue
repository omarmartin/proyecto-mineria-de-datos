<template>
  <div >
    <div>
      <!-- apriori form ===================== -->
        <form class="grid_cancer" id="apriori-form" @submit.prevent="store.enviar_datos" method="POST">
          <!-- support -->
          <div class="id">
            <label class="label">id</label>
            <input type="text" class="input" name="id"  v-model="store.formdata.id">
          </div>
          <div class="radius">
            <label class="label">radius</label>
            <input type="text" class="input" name="radius"  v-model="store.formdata.radius">
          </div>
          <div class="texture">
            <label class="label">texture</label>
            <input type="text" class="input" name="texture"  v-model="store.formdata.texture">
          </div>
          <div class="perimeter">
            <label class="label">perimeter</label>
            <input type="text" class="input" name="perimeter"  v-model="store.formdata.perimeter">
          </div>
          <div class="area">
            <label class="label">area</label>
            <input type="text" class="input" name="area"  v-model="store.formdata.area">
          </div>
          <div class="smoothness">
            <label class="label">smoothness</label>
            <input type="text" class="input" name="smoothness"  v-model="store.formdata.smoothness">
          </div>
          <div class="compactness">
            <label class="label">compactness</label>
            <input type="text" class="input" name="compactness"  v-model="store.formdata.compactness">
          </div>
          <div class="concavity">
            <label class="label">concavity</label>
            <input type="text" class="input" name="concavity"  v-model="store.formdata.concavity">
          </div>
          <div class="concave_points">
            <label class="label">concave points</label>
            <input type="text" class="input" name="concave_points"  v-model="store.formdata.concave_points">
          </div>
          <div class="symmetry">
            <label class="label">symmetry</label>
            <input type="text" class="input" name="symmetry"  v-model="store.formdata.symmetry">
          </div>
          <div class="fractal_dimension">
            <label class="label">fractal dimension</label>
            <input type="text" class="input" name="fractal_dimension"  v-model="store.formdata.fractal_dimension">
          </div>
          <!-- submit button -->
          <div class="boton has-text-right">
            <button class="button is-danger">Submit</button>
          </div>
        </form>
    </div>
    <div>
        <h1>{{store.formdata.reglas}}</h1> 
    </div>
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
.grid_cancer{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(5, 130px); 
  font-size: 1.2rem;
}

.input{
  background-color: beige;
  font-size: 1.2rem;
}

.grid_cancer .id{
  grid-column-start: 1;
  grid-row-start: 1;
  grid-row-end: 1;
  text-align: right;
  font-size: 1rem;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

.grid_cancer .radius{
  grid-column-start: 2;
  grid-row-start: 1;
  text-align: right;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

.grid_cancer .texture{
  grid-column-start: 3;
  grid-row-start: 1;
  text-align: right;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

.grid_cancer .perimeter{
  grid-column-start: 1;
  grid-row-start: 2;
  text-align: right;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

.grid_cancer .area{
  grid-column-start: 2;
  grid-row-start: 2;
  text-align: right;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

.grid_cancer .smoothness{
  grid-column-start: 3;
  grid-row-start: 2;
  text-align: right;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

.grid_cancer .compactness{
  grid-column-start: 1;
  grid-row-start: 3;
  text-align: right;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

.grid_cancer .concavity{
  grid-column-start: 2;
  grid-row-start: 3;
  text-align: right;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

.grid_cancer .concave_points{
  grid-column-start: 3;
  grid-row-start: 3;
  text-align: right;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

.grid_cancer .symmetry{
  grid-column-start: 1;
  grid-row-start: 4;
  text-align: right;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

.grid_cancer .fractal_dimension{
  grid-column-start: 2;
  grid-row-start: 4;
  text-align: right;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

.grid_cancer .boton{
  grid-column-start: 1;
  grid-column-end: 3;
  grid-row-start: 5;
  align-self: top;
  text-align: center;
  margin-left: 500px;
  font-size: 2rem;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}


</style>