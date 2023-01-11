import web3 
from .tokens import eth, dai

w3 = web3.Web3(web3.Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{os.environ['INFURA_KEY']}"))

with open('offchain/uniswap-v3/quoter.abi', 'r') as f:
  quoter_abi = f.read()

uniswap_v3_quoter = w3.eth.contract(address="0xb27308f9F90D607463bb33eA1BeBb41C27CE5AB6", abi=quoter_abi)
print(uniswap_v3_quoter.functions.quoteExactInputSingle(dai, eth, 10**6, 10**18, 0).call())
