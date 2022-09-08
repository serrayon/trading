import json
import requests 
import pandas as pd
import datetime
#pip3 install requests and pandas 

#for limit if you chose 1000 it should be wrapped in a for loop

currency_pair = "btcusd"
url =f" https://www.bitstamp.net/api/v2/ohlc/{currency_pair}/"

start = "2021-01-01"
end = "2021-01-02"
#pandas has the following method 
dates = pd.date_range(start,end,freq = "12H")
#using the dates requests above we now convert the data to a 
#list comprehension in order to get the integer value of the date
#pandas measures time in micro seconds, to convert divide x.value by 10 to the 
#power of 9 and cast it to an integer
dates = [ int(x.value/10**9) for x in list(dates)]
print(dates)

master_data = [ ]

for first, last in zip(dates, dates[1:]):
    #print used to demonstrate the what it grabs per iteration
    #it gives us the pairs as it goes along 1pm-2pm 3pm->4pm
    print(first,last)

    params = { 
            "step":60,
             "limit":1000,
             "start": first,
             "end": last
        } 
    data = requests.get(url, params = params)

    data = (data.json()["data"]["ohlc"])
    master_data += data

df = pd.DataFrame(master_data)
df = df.drop_duplicates()
df["timestamp"] = df["timestamp"].astype(int)
df = df.sort_values(by="timestamp")
df = df[ df["timestamp"] >= dates[0]]
df = df[ df["timestamp"] < dates[-1]]
df["date"] = pd.to_datetime(df["timestamp"])
#this was used to find the initial data blocks 
#then saved it to data and created a pandas db 
#to make it easier to read
'''print = (data.json()["data"]["ohlc"])'''  
print(df)
print(len(df))

df.to_csv("tradingBot.csv", index=False)
#pandas sometimes pulls data and it thinks its a string we want 
#it to recognize integers


#filteers for dates begining with our range



#when you get the dataframe back copy timestamp and 
#go to epochconverter.com and it will convert it to what 
#it corresponds to

#this will save the file for backtesting
