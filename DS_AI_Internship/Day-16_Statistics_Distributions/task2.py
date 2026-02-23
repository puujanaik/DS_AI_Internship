import numpy as np
import pandas as pd

# ------------------------------
# Generate Sample Dataset
# ------------------------------
np.random.seed(42)

# Normal data
data = np.random.normal(loc=50, scale=10, size=100)

# Add extreme values manually (Outliers)
data = np.append(data, [150, -40])

df = pd.DataFrame({"Value": data})

# ------------------------------
# Calculate Mean and Std Dev
# ------------------------------
mean = df["Value"].mean()
std_dev = df["Value"].std()

print("Mean (μ):", mean)
print("Standard Deviation (σ):", std_dev)
print("-" * 40)

# ------------------------------
# Calculate Z-score
# Z = (x - μ) / σ
# ------------------------------
df["z_score"] = (df["Value"] - mean) / std_dev

# ------------------------------
# Identify Outliers |Z| > 3
# ------------------------------
outliers = df[np.abs(df["z_score"]) > 3]

print("Outliers where |Z| > 3:")
print(outliers)

print("-" * 40)
print("Total Outliers Found:", len(outliers))
