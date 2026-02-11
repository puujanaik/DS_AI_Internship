import pandas as pd

# Create a Series of names
names = pd.Series(['Alice', 'Bob', 'CHARLIE'])

# Convert names to lowercase
print("Lowercase Names:")
print(names.str.lower())

# Find length of each name
print("\nLength of Each Name:")
print(names.str.upper())
