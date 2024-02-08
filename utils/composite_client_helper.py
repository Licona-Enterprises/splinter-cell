from random import randrange
from flask import jsonify
from v4_client_py.clients.dydx_composite_client import CompositeClient
from v4_client_py.clients.dydx_subaccount import Subaccount
from v4_client_py.clients.constants import Network
from v4_client_py.clients.constants import BECH32_PREFIX
from v4_client_py.clients.helpers.chain_helpers import ( OrderType,  OrderSide,  OrderTimeInForce,  OrderExecution)
from v4_client_py.chain.aerial.wallet import LocalWallet
from my_wallet_helper import MyWallet
import my_constants as constants

# composite place trades, TODO cancel orders
class CompositeClientHelper:
    def __init__(self):
        self.client = CompositeClient(
            Network.testnet(),
            # TODO uncomment below to add mainnet Network
            # Network.mainnet(),
        )
        this_wallet = LocalWallet.from_mnemonic(constants.DYDX_MY_MNEMONIC, BECH32_PREFIX)
        self.wallet = MyWallet.get

    def place_order(self):
        this_wallet = LocalWallet.from_mnemonic(constants.DYDX_MY_MNEMONIC, BECH32_PREFIX)
        subaccount = Subaccount(this_wallet, 0)

        print(subaccount)
        # TODO remove hardcodes and create separate class to 
        clientId = 123 # set to a number, can be used by the client to identify the order
        market = "BTC-USD" # perpertual market id
        type = OrderType.LIMIT # order type
        side = OrderSide.BUY # side of the order

        time_in_force = OrderTimeInForce.IOC 
        # time_in_force = OrderTimeInForce.GTT

        time_in_force_seconds = 60
        latest_block = self.client.validator_client.get.latest_block()
        next_valid_block = latest_block.block.header.height + 1
        good_til_block = next_valid_block + 10

        execution = OrderExecution.DEFAULT
        price = 30_000 # price of 30,000;
        size = 0.1 # subticks are calculated by the price of the order
        postOnly = False # If true, order is post only
        reduceOnly = False # if true, the order will only reduce the position size
        triggerPrice = None # required for conditional orders
        
        tx = self.client.place_order(
            # subaccount,
            # market,
            # type,
            # side,
            # price,
            # size,
            # clientId,
            # timeInForce,
            # 0,
            # execution,
            # postOnly,
            # reduceOnly,
            # triggerPrice

            subaccount,
            market='ETH-USD',
            type=type,
            side=side,
            price=price,
            size=0.01,
            client_id=randrange(0, 100000000),
            time_in_force=time_in_force,
            good_til_block=good_til_block,
            good_til_time_in_seconds=time_in_force_seconds,
            execution=OrderExecution.DEFAULT,
            post_only=False,
            reduce_only=False
        )

        return tx


testrun = CompositeClientHelper()
print(testrun.place_order())
    