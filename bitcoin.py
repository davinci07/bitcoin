
import requests as req
import pandas as pd
import json
import csv
import matplotlib.pyplot as plt


# Set pu URL for the program to talk to
def crypto(ticker):
    base = 'https://api.pro.coinbase.com'   # the url base
    qqq = '/products/%s/candles' % (ticker)  # the page  #candles used to be trades -- see coinbase website
    url = base + qqq
    #start = "2017-01-07T23:00:00.000Z"
    #end = "2017-01-08T04:00:00.000Z"

    times = [["2017-01-07T23:00:00.000Z","2017-01-08T04:00:00.000Z"],
    ["2017-01-08T04:00:00.000Z", "2017-01-08T09:00:00.000Z"]]

    df = pd.DataFrame()

    for i in times:
        r = req.get(url=url, params = {'start' : i[0], 'end' : i[1], 'granularity' : 60})
        df = df.append(r.json())

    df.columns=(["time", "low", "high", "open", "close", "volume"])
    df = df.sort_values("time")
    df["time"] = pd.to_datetime(df['time'],unit='s')
    return(df)

    #df.plot(kind='line', x="time", y='open', color="green")
    #plt.show()
    #df = pd.DataFrame(r.json())
    #df.columns=(["time", "low", "high", "open", "close", "volume"])
    #df.to_csv('%s.csv' % (ticker), index=False)

btc_usd = crypto("btc-usd")
ltc_usd = crypto("ltc-usd")
#eth_usd = crypto("eth-usd")

btc_usd["spread"] = btc_usd["open"] - btc_usd["close"]
btc_usd["spread"] = btc_usd["spread"].apply((lambda x: "Negative" if x < 0 else x))
btc_usd.to_csv('%s.csv' % ("btc-usd"), index=False)