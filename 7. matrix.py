import numpy as np

# Initialize the list
a = [[1, 2], [3, 4], [5, 6], [7, 8]]

# Create 2D numpy array
np_a = np.array(a)

# print 2D Numpy Array
print('-> 2D Numpy Array')
print(np_a)

# Print 4th row of the matrix
print('-> 4th row of the matrix')
print(np_a[3, :])

# print 2nd column of the matrix
print('-> 2nd column of the matrix')
print(np_a[:, 1])

# print 4th row's first column
print('-> 4th row\'s first column')
print(np_a[3, 0])
