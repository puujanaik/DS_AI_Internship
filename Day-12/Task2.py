# STEP 1 — Import matplotlib
import matplotlib.pyplot as plt

# STEP 2 — Define categorical sales data
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

# STEP 3 — Define trend data (example: monthly total sales)
months = [1, 2, 3, 4, 5]
monthly_sales = [500, 650, 700, 800, 900]

# STEP 4 — Create first subplot (Bar Chart)
plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

# STEP 5 — Create second subplot (Line Plot)
plt.subplot(1, 2, 2)
plt.plot(months, monthly_sales)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

# STEP 6 — Adjust layout
plt.tight_layout()

# STEP 7 — Show figure
plt.show()
