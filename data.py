import yfinance as yf #download real stock data from Yahoo Finance
import pandas as pd #data manipulation

#gets stock abbrevation
def get_ticker(symbol: str):
    return yf.Ticker(symbol)

"""
Variables:
period = how many years back to get data for (controls how far back you fetch data)
interval = time spacing per minute (controls the spacing of the data)
"""

#gets 10+ year historical data
def get_history(symbol, period = "10y", interval = "1d"):
    ticker = get_ticker(symbol)
    hist = ticker.history(period=period, interval=interval)
    return hist

#gets current stock price using 1 minute interval data
def get_current_price(symbol):
    ticker = get_ticker(symbol)
    intraday = ticker.history(period="1d", interval="1m")

    #none if data missing
    if intraday.empty:
        return None

    return float(intraday["Close"].iloc[-1])

#for getting P/E ratio to do the P/E < 22 check
def get_pe_ratio(symbol):
    ticker = get_ticker(symbol)
    info = ticker.info or {}
    pe = info.get("trailingPE")
    return float(pe) if pe is not None else None