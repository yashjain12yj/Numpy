a = [2,4,6]

import numpy as np

np_a = np.array(a)

mul = 3
div = 2

# multiplication on simple array
print('multiplication on simple array')
mul1 = a * mul
print(mul1)

# multiplication on numpy array
print('multiplication on numpy array')
mul2 = np_a * mul
print(mul2)

# division on simple array
print('division on simple array')
# div1 = a / div
# print(div1)

# Division on numpy array
print('Division on numpy array')
div2 = np_a // div
print(div2)
