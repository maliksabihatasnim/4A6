import numpy as np

# Given values
S = 19            # Stock price
K = 20            # Strike price
C = 1             # Call price
r = 0.03          # Risk-free rate (annual)
T = 4 / 12        # Time to maturity in years

# Calculate the present value of the strike price
K_present = K * np.exp(-r * T)

# Use put-call parity to find the put price
P = C + K_present - S

print(f"European put option price: ${P:.4f}")
