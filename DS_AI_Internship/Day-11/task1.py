# STEP 1 — Import matplotlib
import matplotlib.pyplot as plt

# STEP 2 — Define data
months = [1, 2, 3, 4, 5]
revenue = [2000, 4500, 4000, 7500, 9000]

# STEP 3 — Create line plot
plt.plot(months, revenue)

# STEP 4 — Add title and labels
plt.title("Monthly Revenue Growth")
plt.xlabel("Month")
plt.ylabel("Revenue in USD")

# STEP 5 — Display the plot
plt.show()