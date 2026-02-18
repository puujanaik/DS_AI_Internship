import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Sample housing dataset
data = {
    'Price': [250000, 300000, 150000, 400000, 500000, 1200000, 275000, 320000, 450000, 600000],
    'City': ['Mumbai', 'Delhi', 'Mumbai', 'Bangalore', 'Delhi', 'Mumbai', 
             'Bangalore', 'Delhi', 'Mumbai', 'Bangalore']
}

df = pd.DataFrame(data)

# Histogram with KDE
plt.figure(figsize=(8,5))
sns.histplot(df['Price'], kde=True)
plt.title("Distribution of Housing Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

# Skewness & Kurtosis
print("Skewness:", df['Price'].skew())
print("Kurtosis:", df['Price'].kurt())

# Count Plot
plt.figure(figsize=(6,4))
sns.countplot(x='City', data=df)
plt.title("Count of Houses by City")
plt.show()

# Log Transformation (if skewed)
df['Log_Price'] = np.log(df['Price'])

plt.figure(figsize=(8,5))
sns.histplot(df['Log_Price'], kde=True)
plt.title("Log Transformed Price Distribution")
plt.show()
