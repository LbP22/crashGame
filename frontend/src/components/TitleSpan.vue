<template>
  <span id="title" v-if="status == 'countdown'">
    BE READY FOR A ROUND
  </span>
</template>

<script>
export default {
  props: ['status']
}
</script>

<style scoped>
  span{
    position: absolute;

    font-family: 'Roboto';
    font-style: normal;
    font-weight: 400;
    font-size: 16px;
    line-height: 19px;

    color: rgba(255, 255, 255, 0.4);

    margin-left: 25%;
  }
</style>
