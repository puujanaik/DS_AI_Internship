import pandas as pd

# STEP 1 — Load dataset
df = pd.read_csv("Day-10/locations.csv")

# STEP 2 — Check unique values BEFORE cleaning
print("Before Cleaning:")
print(df["Location"].unique())

# STEP 3 — Remove extra spaces
df["Location"] = df["Location"].str.strip()

# STEP 4 — Standardize case (choose one)
df["Location"] = df["Location"].str.title()
# OR use .str.lower()

# STEP 5 — Check unique values AFTER cleaning
print("\nAfter Cleaning:")
print(df["Location"].unique())
