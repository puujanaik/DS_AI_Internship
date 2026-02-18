import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Step 1: Create sample dataset
data = {
    'Age': [22, 25, 47, 52, 46, 56, 48],
    'Salary': [25000, 32000, 75000, 110000, 98000, 120000, 88000]
}

df = pd.DataFrame(data)

print("Original Data:\n")
print(df)

# -------------------------------
# Step 2: Standardization
# -------------------------------
standard_scaler = StandardScaler()
df_standardized = pd.DataFrame(
    standard_scaler.fit_transform(df),
    columns=df.columns
)

print("\nStandardized Data (Mean=0, Std=1):\n")
print(df_standardized)

# -------------------------------
# Step 3: Normalization
# -------------------------------
minmax_scaler = MinMaxScaler()
df_normalized = pd.DataFrame(
    minmax_scaler.fit_transform(df),
    columns=df.columns
)

print("\nNormalized Data (Range 0-1):\n")
print(df_normalized)

# -------------------------------
# Step 4: Plot Histogram (Salary)
# -------------------------------

plt.figure()
plt.hist(df['Salary'])
plt.title("Original Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.hist(df_standardized['Salary'])
plt.title("Standardized Salary Distribution")
plt.xlabel("Salary (Standardized)")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.hist(df_normalized['Salary'])
plt.title("Normalized Salary Distribution")
plt.xlabel("Salary (0-1)")
plt.ylabel("Frequency")
plt.show()
