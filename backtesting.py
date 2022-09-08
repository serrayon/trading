import numpy as np 
import pandas as pd 
import datetime as datetime
import vectorbt as vbt 

num = 10
metric = "total_return"
btc_price = pd.read_csv('DataWithDate.csv')[["timestamp", "close"]]
btc_price["date"] = pd.to_datetime( btc_price["timestamp"], unit = "s")
#this will bring back the data indexed by the date it occured and adding
#close will remove timestamp 
btc_price = btc_price.set_index("date")["close"]

#basic indicators like MA, EMA are built in 
rsi = vbt.RSI.run(btc_price, window = 14, short_name="rsi")
#this will compare each value in entry points with
#with exit points so 1 and 55 againts each other
entry_points = np.linspace(1,45, num=num)
exit_points = np.linspace(55,99, num=num)
#below was refactored to above
entries = rsi.rsi_crossed_below(list(entry_points))
exits = rsi.rsi_crossed_above(list(exit_points))

pf = vbt.Portfolio.from_signals(btc_price, entries, exits)
#this grabs total returns from different portfolios
pf_perf = pf.deep_getattr(metric)
#print(pf_perf)

pf_perf_matrix = pf_perf.vbt.unstack_to_df(index_levels = "rsi_crossed_above", column_levels = "rsi_crossed_below")
print(pf_perf_matrix)

'''print(pf.stats())
#brings up a new web page with the trade executions ploted out
pf.plot().show()'''

'''
print(exits.to_string())
print(entries.to_string())
print(btc_price)'''