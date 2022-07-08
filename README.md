# HFT market making in pytorch and gym


## Agent
![DQN Agent Diagram](./docs/images/DQN_Trading.png)

Environment State Space is consists of eight indicators: 
1) LOB levels rendered as stationary prices;
2) cumulative notional value at each price level; 
3) imbalances for cumulative notionals;
4) order inflow imbalances at LOB levels; 
5) the spread between the best bid and ask prices; 
6) custom price momentum indicator;
7) custom trade flow imbalance indicator; and 
8) environmental reward signal.


    
    
    
