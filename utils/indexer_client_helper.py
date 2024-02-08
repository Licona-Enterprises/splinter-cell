from flask import jsonify
from v4_client_py.clients.dydx_indexer_client import IndexerClient
from v4_client_py.clients.constants import Network
from v4_client_py.clients.constants import Network
import my_constants as constants

# indexer returns dydx chain and market metrics
class IndexerClientHelper:
    def __init__(self):
        self.client = IndexerClient(
            config=Network.testnet().indexer_config,
            # TODO uncomment below to add mainnet Network
            # config=Network.mainnet().indexer_config,
        )
        
    def get_block_height(self): 
        height_response = self.client.utility.get_height()
        height = height_response.data['height']
        height_time = height_response.data['time']
        return height_response, height, height_time
    
    def get_server_time(self):
        time_response = self.client.utility.get_time()
        time_iso = time_response.data['iso']
        time_epoch = time_response.data['epoch']
        return time_response, time_iso, time_epoch
    
    def list_perpetual_markets(self):
        markets_response = self.client.markets.get_perpetual_markets()
        return markets_response

    def get_perpetual_market(self, ticker):
        markets_response = self.client.markets.get_perpetual_markets(ticker)
        return markets_response
    
    def get_orderbook(self, ticker):
        market_orderbook_response = self.client.markets.get_perpetual_market_orderbook(ticker)
        market_orderbook = market_orderbook_response.data
        market_orderbook_asks = market_orderbook['asks']
        market_orderbook_bids = market_orderbook['bids']
        return market_orderbook, market_orderbook_asks, market_orderbook_bids
    
    def get_user_wallet_info_subaccount_0(self):
        portfolio = {}
        asset_positions_response = self.client.account.get_subaccount_asset_positions(constants.DYDX_MY_ADDRESS, constants.DYDX_MY_SUBACCOUNT_0)
        portfolio['asset_positions'] = asset_positions_response.data['positions']
        perpetual_positions_response = self.client.account.get_subaccount_perpetual_positions(constants.DYDX_MY_ADDRESS, constants.DYDX_MY_SUBACCOUNT_0)
        portfolio['perpetual_positions'] = perpetual_positions_response.data['positions']
        orders_response = self.client.account.get_subaccount_orders(constants.DYDX_MY_ADDRESS, constants.DYDX_MY_SUBACCOUNT_0)
        portfolio['orders_response'] = orders_response.data
        fills_response = self.client.account.get_subaccount_fills(constants.DYDX_MY_ADDRESS, constants.DYDX_MY_SUBACCOUNT_0)
        portfolio['fills_response'] = fills_response.data['fills']
        historical_pnl_response = self.client.account.get_subaccount_historical_pnls(constants.DYDX_MY_ADDRESS, constants.DYDX_MY_SUBACCOUNT_0)
        portfolio['historical_pnl_response'] = historical_pnl_response.data['historicalPnl']
        return portfolio
