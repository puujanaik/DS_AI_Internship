import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample housing dataset
data = {
    'SquareFootage': [800, 1000, 1200, 1500, 1800, 2000, 2200, 2500, 3000, 3500],
    'Price': [200000, 250000, 300000, 400000, 450000, 500000, 550000, 650000, 800000, 950000],
    'City': ['Mumbai', 'Delhi', 'Mumbai', 'Bangalore', 'Delhi',
             'Mumbai', 'Bangalore', 'Delhi', 'Mumbai', 'Bangalore']
}

df = pd.DataFrame(data)


plt.figure(figsize=(8,5))
sns.scatterplot(x='SquareFootage', y='Price', data=df)
plt.title("Square Footage vs Price")
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.show()


plt.figure(figsize=(7,5))
sns.boxplot(x='City', y='Price', data=df)
plt.title("City vs Price Distribution")
plt.show()


correlation = df['SquareFootage'].corr(df['Price'])
print("Correlation between SquareFootage and Price:", correlation)
