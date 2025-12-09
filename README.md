# Investment-Formula
Algorithmic trading
import math
from math import log, sqrt, exp
from typing import Literal

import scipy
from scipy.stats import norm  # install via: pip install scipy


def black_scholes(
    S: float,       # current stock price
    K: float,       # strike price
    T: float,       # time to maturity in years
    r: float,       # risk-free rate (annual, continuous or close)
    sigma: float,   # volatility (annualized standard deviation)
    option_type: Literal["call", "put"] = "call",
) -> float:
    """
    Returns the theoretical Black-Scholes price of a European call or put option.
    """

    if T <= 0:
        # At expiration, option value is just intrinsic value
        if option_type == "call":
            return max(S - K, 0.0)
        else:
            return max(K - S, 0.0)

    if sigma <= 0:
        # Zero volatility degenerates to discounted intrinsic value expectation
        if option_type == "call":
            return max(S - K * exp(-r * T), 0.0)
        else:
            return max(K * exp(-r * T) - S, 0.0)

    d1 = (log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)

    if option_type == "call":
        price = S * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)
    else:  # put
        price = K * exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    return float(price)


# Example usage
if __name__ == "__main__":
    S = 100.0   # stock price
    K = 110.0   # strike
    T = 0.5     # 6 months
    r = 0.05    # 5% risk-free
    sigma = 0.2 # 20% volatility

    call_price = black_scholes(S, K, T, r, sigma, "call")
    put_price = black_scholes(S, K, T, r, sigma, "put")

    print("Call:", call_price)
    print("Put:", put_price)
