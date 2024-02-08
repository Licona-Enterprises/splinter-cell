import asyncio
import json
import requests
from v4_client_py.clients.dydx_socket_client import SocketClient
from v4_client_py.clients.constants import Network
import utils.my_constants as constants


url = 'http://127.0.0.1:105/market_data'

def on_open(ws):
    print('WebSocket connection opened')
    ws.send_ping_if_inactive_for(30)

def on_message(ws, message):
    # print(f'Received message: {message}')
    payload = json.loads(message)
    response = requests.post(url, json=payload)
    print(response.json())
    if (payload['type'] == 'connected'):
        my_ws.subscribe_to_markets()
    ws.send_ping_if_inactive_for(30)
    ws.subscribe_to_markets()

def on_close(ws):
    print('WebSocket connection closed')

my_ws = SocketClient(config=Network.testnet().indexer_config, on_message=on_message, on_open=on_open, on_close=on_close)

async def main():
    my_ws.connect()

    # Do some stuff...

    # my_ws.close()
asyncio.get_event_loop().run_until_complete(main())