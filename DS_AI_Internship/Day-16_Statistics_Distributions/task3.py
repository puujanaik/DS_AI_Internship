import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------
#   Skewed Dataset (Income-like)
# ------------------------------
np.random.seed(42)

population = np.random.exponential(scale=50000, size=10000)

# Plot original distribution
plt.figure()
sns.histplot(population, kde=True)
plt.title("Original Population Distribution (Right-Skewed)")
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.show()

# ------------------------------
# Central Limit Theorem Simulation
# ------------------------------
sample_means = []

for i in range(1000):
    sample = np.random.choice(population, size=30)
    sample_mean = np.mean(sample)
    sample_means.append(sample_mean)

# ------------------------------
#  Plot Distribution of Sample Means
# ------------------------------
plt.figure()
sns.histplot(sample_means, kde=True)
plt.title("Distribution of 1000 Sample Means (n=30)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()


print("Population Mean:", np.mean(population))
print("Mean of Sample Means:", np.mean(sample_means))
