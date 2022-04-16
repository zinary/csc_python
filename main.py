from web3 import Web3
from web3.middleware import geth_poa_middleware

# Web3 provider configuration
provider = Web3.HTTPProvider("https://testnet-rpc.coinex.net")
web3client = Web3(provider)
web3client.middleware_onion.inject(geth_poa_middleware, layer=0)

def get_balance():
    wallet_address = input("Enter the wallet address => ")
    balance_wei = web3client.eth.get_balance(wallet_address)
    balance_ether = web3client.fromWei(balance_wei, 'ether')
    print(f"The $CET balance is : {balance_ether}")

def send_transaction():
    from_address = input("Enter from wallet address => ")
    to_address = input("Enter to wallet address => ")
    private_key = input("Enter your private key to sign the transaction => ")
    nonce = web3client.eth.getTransactionCount(from_address)
    amount = web3client.toWei(1234235, 'ether') #we are going to send 1 CET
    tx = {
        'nonce': nonce,
        'to': to_address,
        'value': amount,
        'gas': 2000000,
        'gasPrice': web3client.eth.gas_price
    }

    signed_tx = web3client.eth.account.sign_transaction(tx, private_key)
    tx_hash = web3client.eth.sendRawTransaction(signed_tx.rawTransaction)

    print(f"Your transaction was successfull. Check details here. https://testnet.coinex.net/tx/{tx_hash.hex()}")
 
if __name__ == "__main__":
    send_transaction()