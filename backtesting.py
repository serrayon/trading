import numpy as np 
import pandas as pd 
import datetime as datetime
import vectorbt as vbt 


btc_price = pd.read_csv('DataWithDate.csv')[["timestamp", "close"]]
btc_price["date"] = pd.to_datetime( btc_price["timestamp"], unit = "s")
#this will bring back the data indexed by the date it occured and adding
#close will remove timestamp 
btc_price = btc_price.set_index("date")["close"]

#basic indicators like MA, EMA are built in 
rsi = vbt.RSI.run(btc_price, window = 14, short_name="rsi")

entries = rsi.rsi_crossed_below(30)
exits = rsi.rsi_crossed_above(70)

pf = vbt.Portfolio.from_signals(btc_price, entries, exits)


print(pf.stats())
#brings up a new web page with the trade executions ploted out
pf.plot().show()

'''
print(exits.to_string())
print(entries.to_string())
print(btc_price)'''