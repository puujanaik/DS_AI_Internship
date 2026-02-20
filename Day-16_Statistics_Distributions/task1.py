import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed
np.random.seed(42)

# -------------------------------
# 1️⃣ Normal Distribution (Heights)
# -------------------------------
heights = np.random.normal(loc=165, scale=7, size=1000)

df_heights = pd.DataFrame({"Heights": heights})

print("Normal Distribution (Heights)")
print("Mean:", df_heights["Heights"].mean())
print("Median:", df_heights["Heights"].median())
print("-" * 40)

plt.figure()
sns.histplot(df_heights["Heights"], kde=True)
plt.title("Normal Distribution - Human Heights")
plt.show()

# -------------------------------
# 2️⃣ Right-Skewed (Income)
# -------------------------------
income = np.random.exponential(scale=50000, size=1000)

df_income = pd.DataFrame({"Income": income})

print("Right-Skewed Distribution (Income)")
print("Mean:", df_income["Income"].mean())
print("Median:", df_income["Income"].median())
print("-" * 40)

plt.figure()
sns.histplot(df_income["Income"], kde=True)
plt.title("Right-Skewed Distribution - Income")
plt.show()

# -------------------------------
# 3️⃣ Left-Skewed (Easy Exam Scores)
# -------------------------------
scores = 100 - np.random.exponential(scale=10, size=1000)

df_scores = pd.DataFrame({"Scores": scores})

print("Left-Skewed Distribution (Scores)")
print("Mean:", df_scores["Scores"].mean())
print("Median:", df_scores["Scores"].median())
print("-" * 40)

plt.figure()
sns.histplot(df_scores["Scores"], kde=True)
plt.title("Left-Skewed Distribution - Easy Exam Scores")
plt.show()
