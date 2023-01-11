from web3 import Web3 
from web3.types import ChecksumAddress
from .tokens import eth, dai

w3 = Web3(provider=f"https://optimism-mainnet.infura.io/v3/{os.environ['INFURA_KEY']}")

with open('offchain/uniswap-v3/quoter.abi', 'r') as f:
  abi = f.read()

quoter = w3.eth.contract("0xE592427A0AEce92De3Edee1F18E0157C05861564", abi=abi)
quoter.functions.quoteExactInputSingle(w3.toChecksumAddress(eth), w3.toChecksumAddress(dai), 0.3, 10**18, 10**18)
