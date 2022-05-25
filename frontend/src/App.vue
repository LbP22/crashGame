<template>
  <div id="app">
    <GridDiv/>
  </div>
</template>

<script>
import GridDiv from '@/components/GridDiv.vue'
export default {
  name: 'App',
  components: {
    GridDiv
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
#app {
  font-family: 'Roboto', sans-serif;
  text-align: center;
}
</style>
