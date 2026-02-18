import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

# ----------------------------------
# Step 1: Create Non-Linear Dataset
# ----------------------------------

# X values
X = np.linspace(-5, 5, 100).reshape(-1, 1)

# Non-linear relationship (quadratic)
y = 3 * (X.flatten() ** 2) + 2 * X.flatten() + 5

# ----------------------------------
# Step 2: Train Simple Linear Model
# ----------------------------------

linear_model = LinearRegression()
linear_model.fit(X, y)

y_pred_linear = linear_model.predict(X)
r2_linear = r2_score(y, y_pred_linear)

# ----------------------------------
# Step 3: Create Polynomial Features
# ----------------------------------

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

poly_model = LinearRegression()
poly_model.fit(X_poly, y)

y_pred_poly = poly_model.predict(X_poly)
r2_poly = r2_score(y, y_pred_poly)

# ----------------------------------
# Step 4: Print R² Scores
# ----------------------------------

print("R² Score (Simple Linear Regression):", round(r2_linear, 4))
print("R² Score (Polynomial Regression Degree 2):", round(r2_poly, 4))

# ----------------------------------
# Step 5: Plot Comparison
# ----------------------------------

plt.figure()
plt.scatter(X, y)
plt.plot(X, y_pred_linear)
plt.title("Simple Linear Regression")
plt.show()

plt.figure()
plt.scatter(X, y)
plt.plot(X, y_pred_poly)
plt.title("Polynomial Regression (Degree 2)")
plt.show()
