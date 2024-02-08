from v4_client_py.chain.aerial.wallet import LocalWallet
from v4_client_py.clients.constants import BECH32_PREFIX
from my_constants import DYDX_MY_ADDRESS, DYDX_MY_PRIVATE_KEY, DYDX_MY_MNEMONIC

class MyWallet:
    def get():
        wallet = LocalWallet.from_mnemonic(mnemonic=DYDX_MY_MNEMONIC, prefix=BECH32_PREFIX)
        private_key = wallet.signer().private_key_hex
        assert(private_key==DYDX_MY_PRIVATE_KEY)
        public_key = wallet.public_key().public_key_hex
        address = wallet.address()
        print(f'public key:{public_key}, address:{address}')
        assert(address==DYDX_MY_ADDRESS)
        return wallet
    


        