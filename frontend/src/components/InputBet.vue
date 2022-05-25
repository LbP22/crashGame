<template>
  <input id="betInput" v-bind:class="{diabledInput: status == 'game' || value > 0 || status == 'crashed' }" v-model="bet" placeholder="BET VALUE">
</template>

<script>
export default {
  props: ['status']
}
</script>

<style>
  input {
    position: absolute;

    width: 132px;
    height: 54px;

    font-family: 'Roboto';
    font-style: normal;
    font-weight: 400;
    font-size: 18px;
    text-align: center;
    align-items: center;

    color: rgba(255, 255, 255, 0.4);
    opacity: 1;
    background: #282B30;
    box-shadow: inset 4px 4px 6px rgba(0, 0, 0, 0.2), inset -4px -4px 6px rgba(255, 255, 255, 0.12);
    border-radius: 15px;

    margin-top: 50%;
    margin-left: 30%;
  }

  .diabledInput {
    opacity: 0.1;
  }

  .enabledInput {
    opacity: 1;
  }

</style>
