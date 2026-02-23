import numpy as np

# Create a 5x3 rows and clmn array of random scores between 50 and 100, Generates random integers from 50 to 100 #NumPy is a numerical library
scores = np.random.randint(50, 101, size=(5, 3))

#  Calculate column-wise mean (mean of each subject)
subject_mean = scores.mean(axis=0)
# axis=0 → column-wise

#  Subtract mean from original scores (broadcasting)
centered_scores = scores - subject_mean

#  Print results 
# Displays the raw student marks
print("Original Scores:")
print(scores)

print("\nMean of each subject:")
print(subject_mean)

print("\nCentered Scores:")
print(centered_scores)