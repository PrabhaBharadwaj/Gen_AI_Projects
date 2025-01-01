# filename: google_amazon_stock_price.py
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical stock price data for Google and Amazon
google_data = yf.download('GOOGL', start='2021-01-01')
amazon_data = yf.download('AMZN', start='2021-01-01')

# Extract the 'Close' price from the data
google_close = google_data['Close']
amazon_close = amazon_data['Close']

# Plotting the stock price change over time for Google and Amazon
plt.figure(figsize=(14, 7))
plt.plot(google_close.index, google_close, label='Google')
plt.plot(amazon_close.index, amazon_close, label='Amazon')
plt.title('Google vs Amazon Stock Price Change')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid()
plt.show()