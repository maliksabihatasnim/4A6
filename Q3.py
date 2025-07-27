import numpy as np
import matplotlib.pyplot as plt

# Given payments and years
years = np.array([1, 2, 3, 4, 5, 6])
payments = np.array([460, 235, 640, 370, 330, 250])

# Given nominal interest rate (compounded quarterly)
nominal_rate = 0.045
compoundings_per_year = 4

# Step 1: Convert to effective annual rate (EAR)
effective_annual_rate = (1 + nominal_rate / compoundings_per_year) ** compoundings_per_year - 1

# Step 2: Calculate present value of each payment
present_values = payments / (1 + effective_annual_rate) ** years
total_present_value = np.sum(present_values)

# Output
print(f"Effective Annual Rate: {effective_annual_rate:.6f}")
print(f"Present Value of each payment: {present_values.round(2)}")
print(f"Total Present Value of the investment: {total_present_value:.2f}")

# Step 3: Visualize payments and their present values
plt.figure(figsize=(10, 5))
plt.bar(years - 0.2, payments, width=0.4, label="Future Payments", color="skyblue")
plt.bar(years + 0.2, present_values, width=0.4, label="Present Values", color="salmon")
plt.xlabel("Year")
plt.ylabel("Amount")
plt.title("Future Payments vs Present Values")
plt.xticks(years)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
