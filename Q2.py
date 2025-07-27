import numpy as np

# Parameters
face_value = 100
coupon_rate = 0.08
r_1 = 0.11  # original yield
r_2 = 0.108  # yield after 0.2% decrease
years = np.arange(1, 6)
coupon = coupon_rate * face_value

# (a) Bond price at r = 11%
cash_flows = [coupon] * 5
cash_flows[-1] += face_value  # Add face value at year 5
pv_flows_1 = [cf * np.exp(-r_1 * t) for cf, t in zip(cash_flows, years)]
price_1 = sum(pv_flows_1)

# (b) Duration
weighted_times = [t * pv for t, pv in zip(years, pv_flows_1)]
duration = sum(weighted_times) / price_1

# (c) Price change due to yield change using duration
delta_r = -0.002  # -0.2%
delta_P_approx = -duration * price_1 * delta_r
approx_new_price = price_1 + delta_P_approx

# (d) Recalculate exact price with new yield (10.8%)
pv_flows_2 = [cf * np.exp(-r_2 * t) for cf, t in zip(cash_flows, years)]
price_2 = sum(pv_flows_2)

# Output
print(f"(a) Bond Price at 11% yield: {price_1:.4f}")
print(f"(b) Duration: {duration:.4f} years")
print(f"(c) Approximate price change: {delta_P_approx:.4f}")
print(f"    Approximate new price: {approx_new_price:.4f}")
print(f"(d) Exact new price at 10.8% yield: {price_2:.4f}")
