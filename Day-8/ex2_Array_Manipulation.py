import numpy as np
# Imports the NumPy library

# Values start from 0 and go up to 11
arr = np.arange(12)
reshaped = arr.reshape(3, 4)
# 3 rows and 4 columns 3 × 4 = 12
print(reshaped)

# vstack() means vertical stack
a = np.array([[1, 2]])
b = np.array([[3, 4]])

# if a b it will print 1234
# if b a it will print 3412  
vstacked = np.vstack((a, b))
print(vstacked)