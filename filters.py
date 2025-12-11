#Runs  P/E < 22 filter and 10-year history checks
# from dataEPS import get_eps_history #for getting the EPS to do the EPS average 7+ years consistency check using FMP api
import numpy as np #stats
from data import get_history, get_pe_ratio #for getting P/E ratio to do the P/E < 22 and 10+ years market data check

#checks if P/E < 22
def pe_filter(symbol, max_pe = 22.0):
    pe = get_pe_ratio(symbol)

    if pe is None:
        print("There's no P/E ratio data available.")
        return False

    if pe < max_pe:
        print(f"Success: P/E = {pe:.2f} (max {max_pe})")
        return True
    else:
        print(f"Fail: P/E = {pe:.2f} (max {max_pe})")
        return False

#Checks if we have 10+ years of historical market data
def history_filter(symbol, min_years = 10):
    hist = get_history(symbol, period=f"{min_years}y", interval="1d")

    if hist.empty:
        print(f"No historical data returned for {symbol}.")
        return False

    #Check time span from first to last date
    days_span = (hist.index[-1] - hist.index[0]).days

    if days_span >= min_years * 365 * 0.9:  #slack
        print(f"Has 10+ years of data")
        return True
    else:
        print(f"Doesn't have 10+ years of data")
        return False

"""
#Checks EPS consistency over 7+ years
def eps_consistency_filter(symbol: str, min_years: int = 7) -> bool:

    eps_series = get_eps_series(symbol)

    if eps_series is None or eps_series.empty:
        print("No EPS/earnings data available.")
        return False

    if len(eps_series) < min_years:
        print(f"Not enough EPS data: have {len(eps_series)}, need {min_years}.")
        return False

    last_n = eps_series[-min_years:]

    if (last_n <= 0).any():
        print("EPS consistency filter failed: negative or zero earnings found.")
        return False

    variance = np.var(last_n.values)

    if variance > (last_n.mean() ** 2) * 1.5:
        # Arbitrary rule: variance is not too huge relative to mean^2
        print(f"EPS consistency filter failed: variance too high ({variance:.2e}).")
        return False

    print(
        f"Passed EPS consistency filter over last {min_years} years "
        f"(mean ≈ {last_n.mean():.2f}, var ≈ {variance:.2e})"
    )
    return True
"""

def passes_all_filters(symbol):
    """
    Run all filters and return True only if the stock passes every one.
    """
    print(f"\nEvaluating fundamentals for {symbol}")

    if not pe_filter(symbol):
        return False

    if not history_filter(symbol, min_years=10):
        return False
    
    """
    if not eps_consistency_filter(symbol, min_years=7):
        return False
    """
    
    print(f"{symbol} PASSED all fundamental filters.")
    return True


