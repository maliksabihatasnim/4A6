import numpy as np

# (a) Initial conditions
S0 = 40             # initial stock price
r = 0.10            # annual risk-free rate, continuous compounding
T = 1               # time in years

# Forward price at initiation
F0 = S0 * np.exp(r * T)
V0 = 0  # fair contract, so no value at initiation

print(f"(a) Forward price at initiation: ${F0:.2f}")
print(f"    Initial value of the forward contract: ${V0:.2f}")

# (b) Six months later
t = 0.5             # time passed
St = 45             # stock price at 6 months
T_t = T - t         # time remaining

# Forward price now
Ft = St * np.exp(r * T_t)

# Value of the contract now
Vt = St - F0 * np.exp(-r * T_t)

print(f"(b) New forward price at t=0.5: ${Ft:.2f}")
print(f"    Value of the forward contract: ${Vt:.2f}")
