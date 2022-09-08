import numpy as np 
import pandas as pd 
import datetime as datetime
import vectorbt as vbt 


btc_price = pd.read_csv('NewData.csv')[["timestamp", "close"]]
btc_price["date"] = pd.to_datetime( btc_price["timestamp"], unit = "s")
print(btc_price)