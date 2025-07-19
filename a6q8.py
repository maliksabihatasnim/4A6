import numpy as np
import pandas as pd
from scipy.stats import norm

# Parameters
S = 32        # Current stock price
r = 0.05      # Risk-free rate
sigma = 0.30  # Volatility
K1, K2, K3 = 25, 30, 35
T_half = 0.5  # 6 months
T_one = 1.0   # 1 year

# Black-Scholes formula
def black_scholes(S, K, T, r, sigma, option_type="call"):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    if option_type == "call":
        return S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
    elif option_type == "put":
        return K*np.exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1)

# Option prices
C25_6m = black_scholes(S, K1, T_half, r, sigma, "call")
C30_6m = black_scholes(S, K2, T_half, r, sigma, "call")
P25_6m = black_scholes(S, K1, T_half, r, sigma, "put")
P30_6m = black_scholes(S, K2, T_half, r, sigma, "put")

C25_1y = black_scholes(S, K1, T_one, r, sigma, "call")
C30_1y = black_scholes(S, K2, T_one, r, sigma, "call")
C35_1y = black_scholes(S, K3, T_one, r, sigma, "call")
P25_1y = black_scholes(S, K1, T_one, r, sigma, "put")
P30_1y = black_scholes(S, K2, T_one, r, sigma, "put")
P35_1y = black_scholes(S, K3, T_one, r, sigma, "put")

# Costs of strategies
cost_bull = C25_6m - C30_6m
cost_bear = P30_6m - P25_6m
cost_butterfly_call = C25_1y - 2*C30_1y + C35_1y
cost_butterfly_put = P25_1y - 2*P30_1y + P35_1y
cost_straddle = C30_6m + P30_6m
cost_strangle = C35_6m + P25_6m if (C35_6m:=black_scholes(S,K3,T_half,r,sigma,"call")) else 0

# Profit tables
S_range = np.arange(15, 46, 1)
def bull_spread_profit(ST):
    return np.maximum(ST-K1,0) - np.maximum(ST-K2,0) - cost_bull
def bear_spread_profit(ST):
    return np.maximum(K2-ST,0) - np.maximum(K1-ST,0) - cost_bear
def butterfly_call_profit(ST):
    return (np.maximum(ST-K1,0) - 2*np.maximum(ST-K2,0) + np.maximum(ST-K3,0)) - cost_butterfly_call
def butterfly_put_profit(ST):
    return (np.maximum(K1-ST,0) - 2*np.maximum(K2-ST,0) + np.maximum(K3-ST,0)) - cost_butterfly_put
def straddle_profit(ST):
    return (np.maximum(ST-K2,0) + np.maximum(K2-ST,0)) - cost_straddle
def strangle_profit(ST):
    return (np.maximum(ST-K3,0) + np.maximum(K1-ST,0)) - cost_strangle

strategies = {
    "Bull Spread (Call)": bull_spread_profit,
    "Bear Spread (Put)": bear_spread_profit,
    "Butterfly (Call)": butterfly_call_profit,
    "Butterfly (Put)": butterfly_put_profit,
    "Straddle": straddle_profit,
    "Strangle": strangle_profit,
}

# Create tables
tables = {}
for name, func in strategies.items():
    tables[name] = pd.DataFrame({
        "Stock Price": S_range,
        "Profit": [func(ST) for ST in S_range]
    })

# Display costs and one example table
print("Costs of Strategies:")
print(f"(a) Bull Spread: {cost_bull:.4f}")
print(f"(b) Bear Spread: {cost_bear:.4f}")
print(f"(c) Butterfly (Call): {cost_butterfly_call:.4f}")
print(f"(d) Butterfly (Put): {cost_butterfly_put:.4f}")
print(f"(e) Straddle: {cost_straddle:.4f}")
print(f"(f) Strangle: {cost_strangle:.4f}")

print("\nBull Spread Profit Table:")
print(tables["Bull Spread (Call)"].to_string(index=False))
