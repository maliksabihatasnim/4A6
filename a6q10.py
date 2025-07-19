import math

# Given parameters
F0 = 60
K = 60
sigma = 0.30
r = 0.08
T = 0.5   # 6 months
n = 2
dt = T / n

# Step 1: Calculate u, d, and p
u = math.exp(sigma * math.sqrt(dt))
d = 1 / u
p = (math.exp(r * dt) - d) / (u - d)

# Step 2: Build futures price tree
F = [[0]*(i+1) for i in range(n+1)]
F[0][0] = F0
for i in range(1, n+1):
    for j in range(i+1):
        F[i][j] = F0 * (u**(i-j)) * (d**j)

# Step 3: Option value at maturity
C = [max(F[n][j] - K, 0) for j in range(n+1)]

# Step 4: Work backward for European option
for i in range(n-1, -1, -1):
    C = [math.exp(-r * dt) * (p * C[j] + (1-p) * C[j+1]) for j in range(i+1)]

european_call_price = C[0]

print(f"European Call Price: {european_call_price:.4f}")
print("American call on futures is never exercised early (same price as European).")
