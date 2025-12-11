# #ignore this file ykw why

# import yfinance as yf #downloads real stock data from Yahoo Finance
# import os
# import requests
# import pandas as pd
# from dotenv import load_dotenv

# #load API key from .env file
# load_dotenv()
# FMP_KEY = os.getenv("FMP_API_KEY")

# #if no key -> error
# if FMP_KEY is None:
#     raise ValueError("No FMP key found")

# #get 7+ years EPS using FMP API
# def get_eps_history(symbol):
#     url = (
#         f"https://financialmodelingprep.com/api/v3/income-statement/"
#         f"{symbol.upper()}?limit=120&apikey={FMP_KEY}"
#     )

#     try:
#         response = requests.get(url)
#         data = response.json()
#     except Exception:
#         return None

#     #for if API returns an error or empty list
#     if not isinstance(data, list) or len(data) == 0:
#         return None

#     #get year + EPS
#     records = []
#     for entry in data:
#         year = entry.get("calendarYear")
#         eps = entry.get("eps")

#         if year is not None and eps is not None:
#             records.append((int(year), float(eps)))

#     if len(records) == 0:
#         return None

#     #convert into a pandas Series
#     df = pd.DataFrame(records, columns=["Year", "EPS"])
#     df = df.sort_values("Year")  #sort oldest to newest
#     df.set_index("Year", inplace=True)

#     eps_series = df["EPS"]
#     eps_series.name = f"{symbol.upper()}_EPS_History"

#     return eps_series

# def get_ticker(symbol: str):
#     return yf.Ticker(symbol)

# #for getting the EPS to do the EPS average 7+ years consistency check using FMP api
# def get_eps_history(symbol):
#     """
#     Get yearly EPS (approx) from earnings data.
#     yfinance gives a DataFrame with 'Earnings' and 'Revenue' by year.
#     We'll treat 'Earnings' / shares as EPS-ish, but for simplicity,
#     we just use 'Earnings' as a proxy series to check consistency.
#     """
#     ticker = get_ticker(symbol)
#     earnings = ticker.earnings  #DataFrame: index = years, columns: Earnings, Revenue

#     if earnings is None or earnings.empty:
#         return None

#     #use the 'Earnings' column as our EPS-like series
#     eps_series = earnings["Earnings"]
#     eps_series.name = "EPS_Proxy"
#     return eps_series
