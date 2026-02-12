# STEP 1 — Import pandas
import pandas as pd

# STEP 2 — Load the dataset
df = pd.read_csv("Day-10/customer_orders.csv")


# STEP 3 — Print shape BEFORE cleaning
print("Shape before cleaning:", df.shape)

# STEP 4 — Check missing values
print("\nMissing values report:")
print(df.isna().sum())

# STEP 5 — Fill missing numeric columns with median
numeric_cols = df.select_dtypes(include='number').columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# STEP 6 — Remove duplicate rows (all columns match)
df = df.drop_duplicates()

# STEP 7 — Print shape AFTER cleaning
print("\nShape after cleaning:", df.shape)
