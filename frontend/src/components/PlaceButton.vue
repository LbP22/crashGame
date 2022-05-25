<template>
  <button id="btnPlaceBet" v-bind:class="{disabled: ((bet == 0 || bet == null) && status == 'game') || (status == 'countdown' && bet > 0 ) || status == 'crashed' }" v-if="!(status == 'game') || (bet == 0 || bet == null)">
    PLACE A BET
  </button>
  <button id="btnTake" class="gameTake" v-bind:class="{disabled: isTake}" v-else-if="status == 'game' && bet > 0" >
    TAKE
  </button>
</template>

<script>
export default {
  props: ['status', 'bet', 'isTake', 'balance']
}
</script>

<style scoped>
  button {
    width: 83px;
    height: 83px;

    font-style: normal;
    font-weight: 700;
    font-size: 14px;
    line-height: 16px;

    color: rgba(255, 255, 255, 0.4);

    background: #292C33;
    border: 0;
    border-radius: 50%;

    margin-top: 47%;
    margin-left: 70%;
  }

  button:active:before {
    box-shadow: inset 4px 4px 20px rgba(255, 255, 255, 0.12), inset -4px -4px 20px rgba(0, 0, 0, 0.25);
  }

  button:active {
    box-shadow: 5px 5px 20px rgba(0, 0, 0, 0.3), -5px -5px 20px rgba(255, 255, 255, 0.12), inset -4px -4px 10px rgba(255, 255, 255, 0.12), inset 4px 4px 10px rgba(0, 0, 0, 0.25);
  }

  .disabled {
    opacity: 0.1;
    box-shadow: 0;
  }

  .gameTake {
    background: #882424;
    box-shadow: inset 4px 4px 20px rgba(255, 255, 255, 0.12), inset -4px -4px 20px rgba(0, 0, 0, 0.25);

    margin-top: 47%;
    margin-left: 70%;
  }

  span {
    position: absolute;

    width: 93px;
    height: 93px;

    font-style: normal;
    font-weight: 700;
    font-size: 14px;
    line-height: 16px;

    color: rgba(255, 255, 255, 0.4);

    box-shadow: 5px 5px 20px rgba(0, 0, 0, 0.3), -5px -5px 20px rgba(255, 255, 255, 0.12), inset -4px -4px 10px rgba(255, 255, 255, 0.12), inset 4px 4px 10px rgba(0, 0, 0, 0.25);
    background: #292C33;
    border: 3px;
    border-radius: 50%;
    margin-top: 47%;
    margin-left: 70%;
  }

</style>
