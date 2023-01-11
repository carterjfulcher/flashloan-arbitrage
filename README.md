# DEX Arbitrage 

**How This Works**

This project combines [Flashloans](https://www.moonpay.com/blog/defi-flash-loans-explained#:~:text=most%20common%20applications.-,What%20are%20flash%20loans%3F,the%20money%20to%20the%20lender.) and Cross Exchange Arbitrage. Utilizing flash loans, a large sum of money can be borrowed and use to purchase assets on one exchange, sell it on another exchange, and use the proceeds to pay the flash loan back with interest, while sending any additional profit back to the smart contract. 

**Observations**:  
- L1 Arbitrage is profitable at low quantities (i.e. <0.1 eth) but infeasible due to high gas fees 
- L2 Arbitrage seems to solve issue of high gas fees, but arbitrage oporunities are not immediately present 
- Both L1 and L2 swaps become horribly innefecient at higher bid sizes (> 1eth) due to price impact or slippage, not sure which
- Lower liquidity in L2 (10% of mainnet)

**Hypotheses**:
- L2 Arbitrage is already priced in, i.e. somebody is already doing this 
- Increasing order size does not increase profit 

**Questions**:  
- Why is there such high slippage at higher buy qtys? Is there a way to improve? 
- Does setting a lower gas limit make the arbitrage opporunity too slow? 


**Data That Would Be Useful**:
- a list of the LP's with the highest liquidity and best prices @ L2 
- breakdown of gas fees, slippage, trade costs, etc. 
