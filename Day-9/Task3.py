import pandas as pd

# Create the Series
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

# Remove extra spaces and convert to lowercase
cleaned_usernames = usernames.str.strip().str.lower()

# Print the cleaned Series
print("Cleaned Usernames:")
print(cleaned_usernames)

# Check which names contain the letter 'a'
contains_a = cleaned_usernames.str.contains('a')

print("\nContains letter 'a':")
print(contains_a)
