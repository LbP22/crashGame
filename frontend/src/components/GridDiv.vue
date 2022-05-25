<template>
  <div>
    <TitleSpan
      v-bind:status="status"
    />
    <TimerSpan
      v-bind:countdown="countdown" v-bind:multiplier="multiplier" v-bind:bet="bet" v-bind:isTake="isTake" v-bind:wonMultiplier="wonMultiplier" v-bind:status="status"
    />
    <hr>
    <span class="balanceTextSpan">
        BALANCE
    </span>
    <BalSumSpan
      v-bind:balance="balance"
    />
    <InputBet
      v-bind:status="status"
    />
    <PlaceButton
       v-on:click="buttonClicked" v-bind:balance="balance" v-bind:bet="bet" v-bind:isTake="isTake" v-bind:status="status"
    />
  </div>
</template>

<script>
import TitleSpan from '@/components/TitleSpan.vue'
import TimerSpan from '@/components/TimerSpan.vue'
import BalSumSpan from '@/components/BalSumSpan.vue'
import PlaceButton from '@/components/PlaceButton.vue'
import InputBet from '@/components/InputBet.vue'

export default {
  data () {
    return {
      countdown: 5,
      multiplier: 1.0,
      balance: 100,
      bet: 0,
      isTake: false,
      wonMultiplier: null,
      status: 'crash',
      ws: null
    }
  },
  components: {
    TitleSpan,
    TimerSpan,
    BalSumSpan,
    PlaceButton,
    InputBet
  },
  mounted () {
    this.ws = new WebSocket('ws://localhost:8765')

    this.ws.onmessage = (event) => {
      var jsonMessage = JSON.parse(event.data)
      switch (jsonMessage.operation) {
        case 'countdown':
          this.status = jsonMessage.operation
          this.countdown = jsonMessage.countdown
          break
        case 'game':
          this.status = jsonMessage.operation
          this.multiplier = jsonMessage.multiplier
          document.getElementById('betInput').disabled = true
          document.getElementById('placeBet').disabled = true
          break
        case 'crashed':
          this.status = jsonMessage.operation
          this.balance = jsonMessage.balance
          break
        case 'restart':
          this.isTake = false
          this.wonMultiplier = null
          this.bet = 0
          document.getElementById('betInput').value = 0
          document.getElementById('betInput').disabled = false
          document.getElementById('placeBet').disabled = false
          break
        default:
          break
      }
    }
  },
  methods: {
    buttonClicked () {
      if (this.status === 'game' && this.bet > 0 && !this.isTake) {
        this.ws.send(JSON.stringify({ operation: 'take' }))
        this.isTake = true
        this.wonMultiplier = this.multiplier
      }
      if (this.status === 'countdown' && this.bet === 0) {
        if (document.getElementById('betInput').value < this.balance && document.getElementById('betInput').value > 0) {
          this.bet = document.getElementById('betInput').value
          this.balance -= this.bet
          this.ws.send(JSON.stringify({ operation: 'betPlaced', value: this.bet }))
          document.getElementById('betInput').className = 'diabledInput'
          document.getElementById('betInput').disabled = true
        }
      }
    }
  }
}
</script>

<style scoped>
  div{
    position: relative;

    width: 450px;
    height: 360px;

    background: #34393D;
    border: 3px solid #3D4249;
    box-shadow: inset 20px 30px 60px 1px #25282D;
    border-radius: 20px;

    margin: 10% auto 10% auto;
    padding-top: 5%;
  }

  hr {
    position: absolute;

    width: 444px;

    border: 3px solid #1D1E24;

    margin-left: 0%;
    margin-top: 35%;
  }

  .balanceTextSpan {
    position: absolute;

    font-family: 'Roboto';
    font-weight: 400;
    font-size: 16px;
    line-height: 19px;
    color: rgba(255, 255, 255, 0.4);

    margin-top: 50%;
    margin-left: 3%;
  }
</style>
