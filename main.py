import yfinance as yf
import pandas as pd

stocks = ["AAPL", "MSFT", "TSLA", "AMZN", "NVDA"]

for stock in stocks:
    data = yf.download(stock, period="1mo", interval="1d")
    last_price = data["Close"].iloc[-1]
    print(f"{stock}: {round(last_price, 2)} USD")
