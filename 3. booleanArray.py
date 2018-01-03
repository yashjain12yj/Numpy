a = [1, 2, 3, 4, 5, 6, 7, 8]

import numpy as np

np_a = np.array(a)

# create boolean array
ans = np_a % 2 == 0

# print boolean array
print('-> Boolean array')
print(ans)

# print even numbers
print('-> Array of boolean')
print(np_a[ans])
