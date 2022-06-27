import datetime as dt
from doctest import DocFileSuite
from mimetypes import init
import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib import style 
import pandas as pd
import pandas_datareader
import pandas_datareader.data as web   
from pandas_datareader._utils import RemoteDataError 

str_arr = input('Enter stock tickers: ').split(',') 
arr = [num.strip().upper() for num in str_arr]

print(arr)


#df = web.DataReader(['aapl', 'googl'], 'yahoo', dt.datetime(2022, 1, 1), dt.datetime.today()).reset_index()

#adj_closings = df['Adj Close']

#print(adj_closings.head())


