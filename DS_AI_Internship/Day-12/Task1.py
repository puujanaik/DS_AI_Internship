# STEP 1 — Import matplotlib
import matplotlib.pyplot as plt

# STEP 2 — Define data
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 55, 65, 70, 75, 85, 90, 95]

# STEP 3 — Create scatter plot
plt.scatter(study_hours, scores)

# STEP 4 — Add title and labels
plt.title("Study Hours vs Exam Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Scores")

# STEP 5 — Display plot
plt.show()
