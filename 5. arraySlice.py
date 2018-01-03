import numpy as np

# Initialize list
a = list(range(1, 101))

# create np array
np_a = np.array(a)

print('-> Original Array')
print(np_a)

# Slice np array
print('-> Slice Array')
print(np_a[10: 20])

# Slice np array with interval
print('-> Slce array with interval')
print(np_a[10: 20: 2])
