# #Ignore this file ykw why

# import numpy as np #stats
# from math import log, sqrt, exp #math functions
# from scipy.stats import norm #nomral distribution
# from data import get_history, get_current_price #price history from Yahoo Finance

# """
# Variables: 
# S = current stock price
# K = strike price
# RD = domestic risk free interest rate (use decimal)
# RF = foreign risk free interest rate (use decimal)
# T = time to maturity (what does that even mean)
# sigma = volatility of FX rate
# option_type = "call" (buy) or "put" (sell)
# """


# def black_scholes(S, K, RD, RF, T, sigma, option_type):

#     #make sure variables (S, K, T, or sigma) are positive
#     if S <= 0 or K <= 0 or T <= 0 or sigma <= 0:
#         raise ValueError("Error: S, K, T, and sigma aren't positive.")
    
#     #probability the option expires in the money (Probability the option is worth something today)
#     d1 = (log(S / K) + (RD - RF + (sigma**2)/2) * T) / (sigma * sqrt(T))

#     #probability it will actually be exercised, adjusting for randomness (Probability the stock beats the strike at expiration)
#     d2 = d1 - sigma * sqrt(T)
    
#     #call (buy) price formula
#     c = S * exp(-RF * T) * norm.cdf(-d1) - K * exp(-RD * T) * norm.cdf(-d2)

#     #pull (sell) price formula
#     p = K * exp(-RD * T) * norm.cdf(d2) - S * exp(-RF * T) * norm.cdf(d1)

# #find sigma (volatility) from historical prices
# def find_sigma(symbol):
#     #ASK DANIEL ABOUT THIS PART????
#     pass

# #estimate fair price of stock
# def fair_price_estimation(symbol):
    
#     #gets current stock price
#     S = get_current_price(symbol)

#     if S is None:
#         print("Could not retrieve current price.")
#         return None