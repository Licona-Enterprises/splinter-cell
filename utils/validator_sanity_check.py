import asyncio
import logging
from random import randrange
from v4_client_py.chain.aerial.wallet import LocalWallet
from v4_client_py.clients.dydx_composite_client import CompositeClient, Subaccount
from v4_client_py.clients.constants import BECH32_PREFIX, Network
from v4_client_py.clients.dydx_validator_client import ValidatorClient
from v4_client_py.clients.helpers.chain_helpers import (
    OrderSide, 
)
from utils_test import loadJson, orderExecutionToTimeInForce
from my_constants import DYDX_MY_MNEMONIC
import my_constants as constants

async def main() -> None:
    network = Network.testnet()
    validator_client = ValidatorClient(network.validator_config)
    address = constants.DYDX_MY_ADDRESS
    try:
        acc = validator_client.get.account(address=address)
        print('account:')
        print(acc)
    except Exception as e:
        print('failed to get account')
        print(e)

    await asyncio.sleep(5)  # wait for placeOrder to complete

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())