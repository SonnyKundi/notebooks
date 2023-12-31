# -*- coding: utf-8 -*-
"""StockMarket.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uDP7x1WNerGaZmOB_JBlH8k9fWZCweqX
"""

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

apple = yf.Ticker("AAPL")

!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json

import json
with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable
    #print("Type:", type(apple_info))
apple_info

apple_info['country']

apple_share_price_data = apple.history(period="max")

apple_share_price_data.head()

"""#reset the index of the DataFrame"""

apple_share_price_data.reset_index(inplace=True)

apple_share_price_data.plot(x="Date", y="Open")

"""Extracting Dividends"""

apple.dividends

apple.dividends.plot()