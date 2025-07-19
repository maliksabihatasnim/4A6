import numpy as np
from scipy.stats import norm

# Given data
S = 30          # Stock price
K = 29          # Strike price
r = 0.05        # Risk-free interest rate
sigma = 0.25    # Volatility
T = 4 / 12      # Time to maturity in years (4 months)

# Black-Scholes formulas for European Call and Put
def black_scholes_call(S, K, r, sigma, T):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price

def black_scholes_put(S, K, r, sigma, T):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put_price

# (a) European Call price
call_price = black_scholes_call(S, K, r, sigma, T)

# (b) American Call price (no dividends -> same as European call)
american_call_price = call_price

# (c) European Put price
put_price = black_scholes_put(S, K, r, sigma, T)

# (d) Put-Call Parity check: C + K*e^{-rT} ?= P + S
lhs = call_price + K * np.exp(-r * T)
rhs = put_price + S
put_call_parity = np.isclose(lhs, rhs)

print(f"European Call Price: ${call_price:.4f}")
print(f"American Call Price: ${american_call_price:.4f}")
print(f"European Put Price: ${put_price:.4f}")
if put_call_parity:
    print("Put-Call Parity holds.")
else:
    print("Put-Call Parity does not hold.")

