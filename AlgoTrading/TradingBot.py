import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math
from secret import IEX_CLOUD_API_TOKEN

sp500_stocks = pd.read_csv('sp_500_stocks.csv')
final_columns = ['Ticker', 'Stock Price', 'Market Cap', 'Numbers of Share to Buy']
update_dataframe = pd.DataFrame(columns=final_columns)

base_url = 'https://sandbox.iexapis.com'
symbol = 'AAPL'
token = IEX_CLOUD_API_TOKEN
path = f"/stable/stock/{symbol}/quote/?token={token}"
url = base_url + path
data = requests.get(url).json()
stockPrice = data['latestPrice']
marketCap = data['marketCap']/1000000000000

# insert_df = pd.DataFrame(pd.Series([symbol, stockPrice, marketCap, 'N/A']), index=final_columns).T
final_dataframe = update_dataframe.append([pd.Series([symbol, stockPrice, marketCap, 'N/A'], index=final_columns)], ignore_index=True)
print(final_dataframe)