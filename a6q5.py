import numpy as np
import matplotlib.pyplot as plt

# Constants
K = 150  # Strike price
P = 5    # Premium
S = np.linspace(100, 200, 1000)  # Range of stock prices

# Payoffs and Profits
# Long Call
long_call_payoff = np.maximum(0, S - K)
long_call_profit = long_call_payoff - P

# Short Call
short_call_payoff = -np.maximum(0, S - K)
short_call_profit = short_call_payoff + P

# Long Put
long_put_payoff = np.maximum(0, K - S)
long_put_profit = long_put_payoff - P

# Short Put
short_put_payoff = -np.maximum(0, K - S)
short_put_profit = short_put_payoff + P

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.subplots_adjust(hspace = 0.42, wspace = 0.217,top = 0.85)

# (a) Long Call
axs[0, 0].plot(S, long_call_payoff,linewidth = 3, label='Payoff')
axs[0, 0].plot(S, long_call_profit,linewidth = 3, label='Profit')
axs[0, 0].set_title('Long Call')
axs[0, 0].legend()
axs[0, 0].grid(True)
axs[0, 0].set_xlabel('Stock Price (S)',loc = 'right')

# (b) Short Call
axs[0, 1].plot(S, short_call_payoff,linewidth = 3, label='Payoff')
axs[0, 1].plot(S, short_call_profit,linewidth = 3, label='Profit')
axs[0, 1].set_title('Short Call')
axs[0, 1].legend()
axs[0, 1].grid(True)
axs[0, 1].set_xlabel('Stock Price (S)',loc = 'right')

# (c) Long Put
axs[1, 0].plot(S, long_put_payoff,linewidth = 3, label='Payoff')
axs[1, 0].plot(S, long_put_profit,linewidth = 3, label='Profit')
axs[1, 0].set_title('Long Put')
axs[1, 0].legend()
axs[1, 0].grid(True)
axs[1, 0].set_xlabel('Stock Price (S)',loc = 'right')

# (d) Short Put
axs[1, 1].plot(S, short_put_payoff,linewidth = 3, label='Payoff')
axs[1, 1].plot(S, short_put_profit,linewidth = 3, label='Profit')
axs[1, 1].set_title('Short Put')
axs[1, 1].legend()
axs[1, 1].grid(True)
axs[1, 1].set_xlabel('Stock Price (S)',loc = 'right')

plt.suptitle("Payoff and Profit Diagrams for Options (K=150, Premium=5)", fontsize=16)

plt.show()
