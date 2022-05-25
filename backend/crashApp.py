import asyncio
import websockets
import json
from random import randint


async def operation_handler(websocket):
    async for message in websocket:
        data = json.loads(message)
        if data['operation'] == 'betPlaced':
            websocket.bet = float(data['value'])
        if data['operation'] == 'take':
            websocket.wonMultiplier = websocket.multiplier
            websocket.take = True


async def app(websocket):
    websocket.bet = 0
    websocket.take = False
    websocket.wonMultiplier = 1.0
    websocket.countdown = 5
    websocket.multiplier = 1.0

    while True:
        operation = 'countdown'
        data_countdown = {
            'operation': operation,
            'countdown': websocket.countdown
        }
        await websocket.send(json.dumps(data_countdown))
        await asyncio.sleep(1)
        websocket.countdown -= 1

        if websocket.countdown == 0:
            operation = 'game'
            crash = randint(101, 1000) * 0.01
            if websocket.bet > websocket.balance:
                websocket.bet = 0
            while websocket.multiplier <= crash:
                websocket.multiplier += 0.01
                data_game = {
                    'operation': operation,
                    'multiplier': round(websocket.multiplier, 2)
                     }
                await websocket.send(json.dumps(data_game))
                await asyncio.sleep(0.03)

            if websocket.bet:
                websocket.balance -= websocket.bet
            if websocket.take:
                websocket.balance += websocket.bet * websocket.wonMultiplier
            websocket.countdown = 5
            websocket.multiplier = 1.0
            websocket.bet = 0
            websocket.wonMultiplier = 0
            operation = 'crashed'
            data_crashed = {
                'operation': operation,
                'balance': round(websocket.balance, 2)
            }
            await websocket.send(json.dumps(data_crashed))
            await asyncio.sleep(10)
            data_restart = {'operation': 'restart'}
            await websocket.send(json.dumps(data_restart))


async def connection_handler(websocket):
    websocket.balance = 100

    asyncio.ensure_future(app(websocket))
    await operation_handler(websocket)


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
