# Robinhood-Sprintax-1099B-automator
Improving sprintax's shit implementation of 1099-B reporting. Especially useful if you are an international and use RobinHood and recieved a consolidated 1099.


## Chrome Driver Dependency!
I used version `90.0.4430.24` but use your own version

## Setup
- Download Chrome Driver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- Setup A File called `sec_trades.csv` with all each row as a transaction from your consolidated RobinHood 1099. Follow the column naming format from the `trades.csv` file in this repo
- Do the same for a `cryp_trades.csv` if you traded crypto currencies with RobinHood.
- In `main.py` , adjust details for your brokerage if it is different from RobinHood. Also change the xpath for your state (Currently set to NC, see inline comment)

## Autofilling
- `execute(index,cryp)` will setup and autofill data for the trade with the corresponding index.`cryp` is a flag to switch between filling info for RobinHood Securities LLC and Robinhood Crypto LLC. Default for all `cryp` flags is `False`.
- To queue all trades to autofill, use `loop(start,end,cryp)`. You can also adjust time delay in the loop. 
- For debugging and testing, you can also run `setupInfo()`,`setupTrade()`,`runInfo(cryp)`, and `runTrade(index)`.

