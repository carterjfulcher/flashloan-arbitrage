pragma solidity ^0.8.10;

import { IFlashLoanReceiver } from './IFlashLoanReceiver.sol'

/*
  === Off Chain Process === 
  1. Iteratively search for currencies 
  2. Send contract invocation 
  3. Track balance and PNL 

  ==== On Chain Process ===
  1. Request flashloan
  2. Buy targetCurrency on baseDEX with baseCurrency 
  3. Sell targetCurrency on targetDEX
  4. Repay flashloan
  5. Send profit to original address
*/

contract Arbitrage is IFlashLoanReceiver {
  function executeArbitrage(
    uint loanAmount,
    address baseDEX, 
    address targetDEX, 
    address baseCurrency, 
    address targetCurrency
  ) public {
    
  }
}
