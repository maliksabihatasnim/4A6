import numpy as np

# Given cash flows
cash_flows_A = [225, 215, 250, 225, 205]
cash_flows_B = [220, 225, 250, 250, 210]

# Parameters
r = 0.0433  # continuously compounded annual interest rate
years = np.array([1, 2, 3, 4, 5])  # payment times in years

# Calculate present values
pv_A = np.sum([C * np.exp(-r * t) for C, t in zip(cash_flows_A, years)])
pv_B = np.sum([C * np.exp(-r * t) for C, t in zip(cash_flows_B, years)])

# Print results
print(f"Present Value of Investment A: {pv_A:.2f}")
print(f"Present Value of Investment B: {pv_B:.2f}")

# Decision
if pv_A > pv_B:
    print("Investment A is preferable.")
elif pv_B > pv_A:
    print("Investment B is preferable.")
else:
    print("Both investments are equally good.")
