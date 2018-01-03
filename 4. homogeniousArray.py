import numpy as np

a = [True, 1, 2]
# create numpy array, convert True to 1
np_a = np.array(a)
print(np_a)

b = [2, 3, False]
# create numpy array, convert False to 0
np_b = np.array(b)
print(np_b)

# type coersion
ans = np.array([True, 1, 2]) + np.array([2, 3, False])
print(ans)