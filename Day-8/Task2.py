import numpy as np

#  1D array with values from 0 to 23, total 24 element
# represents 24 sensor readings in a flat list
data = np.arange(24)

#  Reshape into a 3D array of shape (4(batch), 3(rows), 2(colmn))
reshaped_data = data.reshape(4, 3, 2)

#  Transpose the array to shape (4, 2, 3)
transposed_data = reshaped_data.transpose(0, 2, 1)


print("Final Shape:", transposed_data.shape)
print("Final Array:")
print(transposed_data)
