import pandas as pd

# STEP 1 — Load dataset
df = pd.read_csv("Day-10/sales_data.csv")

# STEP 2 — Check initial data types
print("Before conversion:\n")
print(df.dtypes)

# STEP 3 — Remove '$' and convert Price to float
df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)

# STEP 4 — Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# STEP 5 — Check data types after conversion
print("\nAfter conversion:\n")
print(df.dtypes)

print("\nCleaned Data:")
print(df)
