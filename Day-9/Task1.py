import pandas as pd

# Create a Pandas Series with product names as index and prices as values
products = pd.Series([700, 150, 300], index=['Laptop', 'Mouse', 'Keyboard'])

# Print the full Series
print("Full Series:")
print(products)
print()

# Access the price of 'Laptop' using label-based indexing
laptop_price = products['Laptop']
print("Price of Laptop (label-based indexing):")
print(laptop_price)
print()

# Slice the Series to show the first two products using positional indexing
first_two = products[:2]
print("First two products (positional slicing):")
print(first_two)
