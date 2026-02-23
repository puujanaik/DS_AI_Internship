import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Step 1: Create dataset
df = pd.DataFrame({
    'Transmission': ['Automatic', 'Manual', 'Manual', 'Automatic', 'Manual'],
    'Color': ['Red', 'Blue', 'Green', 'Red', 'Blue']
})

print("Original Data:\n")
print(df)

# Step 2: Label Encoding (Binary Column)
le = LabelEncoder()
df['Transmission'] = le.fit_transform(df['Transmission'])

# Step 3: One-Hot Encoding (Nominal Column)
df = pd.get_dummies(df, columns=['Color'], drop_first=True)

print("\nEncoded Data:\n")
print(df)
