import numpy as np

a = [1, 2, 3, 4, 5]

np_a = np.array(a)
np_b = np.array([2, 3, 4, 5, 6])

# mean of the array
print('-> Mean :')
mean = np.mean(np_a)
print(mean)

# median of the array
print('-> Median :')
median = np.median(np_a)
print(median)

# standard deviation
print('-> standard deviation')
std = np.std(np_a)
print(std)

# correlation between two column
print('-> correlation between 2 columns')
corr = np.corrcoef(np_a, np_b)
print(corr)
