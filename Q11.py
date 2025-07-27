import numpy as np

# Given parameters
S = 484        # Current index level
K = 480        # Strike price
r = 0.10       # Risk-free rate
q = 0.03       # Dividend yield
sigma = 0.25   # Volatility
T = 2/12       # Time to maturity in years
N = 4          # Number of steps

# Time per step
dt = T / N

# Up and down factors
u = np.exp(sigma * np.sqrt(dt))
d = 1 / u

# Risk-neutral probability
p = (np.exp((r - q) * dt) - d) / (u - d)

# Initialize stock price tree
stock_tree = np.zeros((N + 1, N + 1))
for i in range(N + 1):
    for j in range(i + 1):
        stock_tree[i, j] = S * (u ** j) * (d ** (i - j))

# Initialize option value tree
option_tree = np.zeros_like(stock_tree)

# Terminal payoffs for put
for j in range(N + 1):
    option_tree[N, j] = max(K - stock_tree[N, j], 0)

# Backward induction for American put
discount = np.exp(-r * dt)
for i in range(N - 1, -1, -1):
    for j in range(i + 1):
        # Expected discounted value
        hold = discount * (p * option_tree[i + 1, j + 1] + (1 - p) * option_tree[i + 1, j])
        # Early exercise value
        exercise = max(K - stock_tree[i, j], 0)
        # Take the maximum for American option
        option_tree[i, j] = max(hold, exercise)

# Print the estimated value of the American put
print(f"Estimated American put option value: {option_tree[0,0]:.4f}")
