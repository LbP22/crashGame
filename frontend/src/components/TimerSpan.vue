<template>
  <span id="countdownSpan" class="countdownSpan" v-if="status == 'countdown'">
    {{countdown}}
  </span>
  <span id="multiplierSpan" class="multiplierSpan" v-else-if="!(status == 'countdown')">
    x{{multiplier.toFixed(2)}}
  </span>
  <span id="crashedSpan" class="crashedSpan" v-if="status == 'crashed' && !isTake">
    CRASHED!
  </span>
  <span id="wonSpan" class="wonSpan" v-if="(status == 'game' || status == 'crashed') && isTake">
    WON {{bet}} x {{wonMultiplier}}
  </span>
</template>

<script>
export default {
  props: ['countdown', 'status', 'multiplier', 'isTake', 'wonMultiplier', 'bet']
}
</script>

<style scoped>
  .countdownSpan {
    position: absolute;

    font-family: 'Roboto';
    font-style: normal;
    font-weight: 400;
    font-size: 40px;
    line-height: 19px;

    color: rgba(255, 255, 255, 0.4);

    margin-left: 42%;
    margin-top: 15%;
  }

  .multiplierSpan {
    position: absolute;

    font-family: 'Roboto';
    font-style: normal;
    font-weight: 700;
    font-size: 55px;
    line-height: 64px;
    display: flex;
    align-items: center;
    text-align: center;

    color: #C27500;

    text-shadow: 2px 4px 6px rgba(0, 0, 0, 0.25);

    margin-left: 35%;
  }

  .crashedSpan {
    position: absolute;

    font-family: 'Roboto';
    font-style: normal;
    font-weight: 700;
    font-size: 30px;
    line-height: 35px;
    display: flex;
    align-items: center;
    text-align: center;

    color: #C20000;

    text-shadow: 2px 4px 6px rgba(0, 0, 0, 0.25);

    margin-top: 20%;
    margin-left: 35%;
}
  .wonSpan {
    position: absolute;

    font-family: 'Roboto';
    font-style: normal;
    font-weight: 700;
    font-size: 30px;
    line-height: 35px;
    display: flex;
    align-items: center;
    text-align: center;

    color: #00C208;

    text-shadow: 2px 4px 6px rgba(0, 0, 0, 0.25);

    margin-top: 20%;
    margin-left: 30%;
  }
</style>
