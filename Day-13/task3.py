import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Sample housing dataset
data = {
    'SquareFootage': [800, 1000, 1200, 1500, 1800, 2000, 2200, 2500, 3000, 3500],
    'Bedrooms': [2, 2, 3, 3, 3, 4, 4, 4, 5, 5],
    'Bathrooms': [1, 1, 2, 2, 2, 3, 3, 3, 4, 4],
    'Price': [200000, 250000, 300000, 400000, 450000, 500000, 550000, 650000, 800000, 2000000]
}

df = pd.DataFrame(data)


corr_matrix = df.corr()
print("Correlation Matrix:\n", corr_matrix)


plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.show()


print("\nHighly Correlated Features (> 0.8):")
for i in range(len(corr_matrix.columns)):
    for j in range(i):
        if abs(corr_matrix.iloc[i, j]) > 0.8:
            print(f"{corr_matrix.columns[i]} and {corr_matrix.columns[j]} -> {corr_matrix.iloc[i, j]}")


plt.figure(figsize=(6,4))
sns.boxplot(y=df['Price'])
plt.title("Boxplot of Price (Outlier Detection)")
plt.show()
