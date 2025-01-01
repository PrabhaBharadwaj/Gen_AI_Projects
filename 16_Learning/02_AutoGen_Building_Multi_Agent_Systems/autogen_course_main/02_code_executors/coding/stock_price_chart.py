# filename: stock_price_chart.py
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical stock price data for META and TESLA
meta_data = yf.download('META', start='2021-01-01')
tesla_data = yf.download('TSLA', start='2021-01-01')

# Extract the 'Close' price from the data
meta_close = meta_data['Close']
tesla_close = tesla_data['Close']

# Plotting the stock price change over time for META and TESLA
plt.figure(figsize=(14, 7))
plt.plot(meta_close.index, meta_close, label='META')
plt.plot(tesla_close.index, tesla_close, label='TESLA')
plt.title('META vs TESLA Stock Price Change')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid()
plt.show()