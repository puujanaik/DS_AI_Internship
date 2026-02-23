# Import the statistics module
# This module provides built-in functions for statistical calculations
import statistics

# Step 1: Define a list of numbers
numbers = [10, 20, 30, 40, 50]

# Step 2: Calculate statistical values
mean_value = statistics.mean(numbers)        # Average of the numbers
median_value = statistics.median(numbers)    # Middle value
variance_value = statistics.variance(numbers)  # Measure of spread
std_dev_value = statistics.stdev(numbers)    # Standard deviation

# Step 3: Display the results in a neat format
print("Statistical Analysis Results")
print("----------------------------")
print(f"Numbers            : {numbers}")
print(f"Mean               : {mean_value}")
print(f"Median             : {median_value}")
print(f"Variance           : {variance_value}")
print(f"Standard Deviation : {std_dev_value}")
