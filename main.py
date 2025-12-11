from filters import passes_all_filters

def main():
    #Check if stock passes all filters
    symbol = input("Stock symbol: ").strip().upper()
    if not passes_all_filters(symbol):
        print(f"{symbol} doesn't pass filters")
        return
"""
#Estimate intrinsic value using Black-Scholes model
    estimate = estimate_intrinsic_value_with_bs(symbol, r=0.04, T=1.0)
    if estimate is None:
        print("Couldn't compute a pricing estimate w/ Black-Scholes")
        return
"""


if __name__ == "__main__":
    main()
