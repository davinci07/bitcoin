# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 19:41:10 2019

@author: Asus
"""

import requests as req
import pandas as pd
import json
import csv

# Set pu URL for the program to talk to

base = 'https://api.pro.coinbase.com'   # the url base
qqq = '/products/BTC-USD/candles'  # the page  #candles used to be trades -- see coinbase website
url = base + qqq


ticks = []
start = "2017-01-07T23:00:00.000Z"
end = "2017-01-07T23:20:00.000Z"

r = req.get(url=url, params = {'start' : start, 'end' : end, 'granularity' : 60})
ticks.append(r.json())

df = pd.DataFrame.from_dict(ticks)
df.to_csv('csv_bitc.csv', index=False)

#with open('bit_csv.csv', 'w',newline='') as fp:
 #   a = csv.writer(fp, delimeter=',')
  #  a.writerows(df)

#for i in range(5):
 #   r = req.get(url=url)
 #   ticks.append(r.json())

#time is unix

#print(pd.DataFrame(ticks))    
    

#print(r.text)
#print(pd.DataFrame.from_dict([r.json()]))


#then go to terminal  #cd.. gets rid of and cd Desktop adds
#python bitcoin.py   in terminal
#b'{  is a json object