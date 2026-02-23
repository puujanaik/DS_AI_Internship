import pandas as pd

# 1. Create the Series with some missing values
grades = pd.Series([85, None, 92, 45, None, 78, 55])

# 2. Print the original Series
print("Original Series:")
print(grades)

# 3. Check which values are missing
print("\nMissing values (True means missing):")
print(grades.isnull())

# 4. Fill missing values with 0
filled_grades = grades.fillna(0)

print("\nSeries after filling missing values with 0:")
print(filled_grades)

# 5. Apply boolean mask: keep only scores > 60
filtered_grades = filled_grades[filled_grades > 60]

print("\nScores greater than 60:")
print(filtered_grades)
