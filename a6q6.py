import numpy as np
import matplotlib.pyplot as plt

# Strike prices and premiums
K_call = 45
K_put = 40
premium_call = 3
premium_put = 4
total_premium = premium_call + premium_put

# Range of asset prices
S = np.linspace(20, 70, 500)

# Payoffs
call_payoff = np.maximum(0, S - K_call)
put_payoff = np.maximum(0, K_put - S)

# Profit = Payoff - Premium
total_profit = call_payoff + put_payoff - total_premium

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(S, total_profit, label='Total Profit', color='b')
plt.plot(S, call_payoff - premium_call, label='Call Payoff', color='orange', linestyle='--',linewidth = 2)
plt.plot(S, put_payoff - premium_put, label='Put Payoff', color='green', linestyle='--',linewidth = 2)

plt.title("Trader's Profit vs Asset Price")
plt.xlabel("Asset Price ($)")
plt.ylabel("Profit ($)")
plt.xticks([K_put, K_call], ['Kp = 40', 'Kc = 45'], fontsize=10)
plt.yticks([premium_call, premium_put], ['c = 3', 'p = 4'], fontsize=10)
plt.legend()
plt.grid(True)
plt.show()
