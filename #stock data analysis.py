#stock data analysis
import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
from pandas_datareader import data as pdr
import yfinance
from datetime import datetime

from __future__ import division

tech_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN']
end = datetime.now()
start = datetime(end.year - 1, end.month, end.day)

for stock in tech_list:
    globals()[stock] = pdr.get_data_yahoo(stock,start,end)

AAPL.describe()


#plots Adj Close price over specified time
AAPL['Adj Close'].plot(legend = True, figsize = (10,4))

#volume
AAPL['Volume'].plot(legend = True, figsize = (10,4

#new syntax python 3
ma_day = [10,20,50]

for ma in ma_day:
    column_name = 'MA for %s days' %(str(ma))
    AAPL[column_name] = pd.Series(AAPL['Adj Close']).rolling(window=ma).mean()

#plots multi moving avg
AAPL[['Adj Close','MA for 10 days','MA for 20 days','MA for 50 days']].plot(subplots=False,figsize=(10,4))

#daily return
AAPL['Daily Return'] = AAPL['Adj Close'].pct_change()
AAPL['Daily Return'].plot(figsize=(12,4), legend=True, linestyle='--', marker='o')

#alt daily returns
sns.distplot(AAPL['Daily Return'].dropna(),bins=100,color='orange')

#or
AAPL['Daily Return'].hist(bins=100)

#new dataframe for all stock in list adj close
closing_df = pdr.get_data_yahoo(['AAPL','GOOG','MSFT','AMZN'],start,end)['Adj Close']

#daily returns
tech_rets = closing_df.pct_change()

sns.jointplot('GOOG','MSFT',tech_rets,kind = 'scatter')

sns.pairplot(tech_rets.dropna())

returns_fig = sns.PairGrid(tech_rets.dropna())
returns_fig.map_upper(plt.scatter, color='orange')
returns_fig.map_lower(sns.kdeplot,cmap='cool_d')
returns_fig.map_diag(plt.hist,bins=30)

returns_fig = sns.PairGrid(closing_df)
returns_fig.map_upper(plt.scatter,color='purple')
returns_fig.map_lower(sns.kdeplot,cmap='cool_d')
returns_fig.map_diag(plt.hist,bins=30)


sns.distplot(AAPL['Daily Return'].dropna(), bins=100,color='green')