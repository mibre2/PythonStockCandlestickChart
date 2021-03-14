import datetime as dt
import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc

# Define Time Frame
start = dt.datetime(2021, 1, 4)     # Start of 2021
end = dt.datetime.now()             # Present TIME

# Load Data
ticker = input('Input ticker symbol: ')     # Prompts user for input of ticker symbol
data = web.DataReader(ticker, 'yahoo', start, end)


# Restructure data
data = data[['Open', 'High', 'Low', 'Close']]
data.reset_index(inplace=True)
data['Date'] = data['Date'].map(mdates.date2num)

# Visualization
ax = plt.subplot()
ax.grid(True)
ax.set_axisbelow(True)
ax.set_title(ticker + ' Share Price'.format(ticker), color='white')
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.xaxis_date()

candlestick_ohlc(ax, data.values, width=0.5, colorup='#008000')
plt.show()
