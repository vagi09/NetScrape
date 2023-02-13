import yfinance as yf
import pandas as pd


apple = yf.Ticker("AAPL")
# print(apple)  #Response

# Stock Info
print(apple.info)

# Maximum Stock Price
print(apple.history(period="max"))

#dividends
print(apple.dividends)