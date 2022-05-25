<template>
  <span id="balanceSpan">
      ${{balance.toFixed(2)}}
  </span>
</template>

<script>
export default {
  props: ['balance']
}
</script>

<style scoped>
  span {
    position: absolute;

    font-family: 'Roboto';
    font-weight: 700;
    font-size: 32px;
    color: rgba(255, 255, 255, 0.4);

    margin-top: 55%;
    margin-left: -2%;
  }
</style>
