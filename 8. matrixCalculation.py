import numpy as np

a = [[1, 2], [3, 4]]
b = [[2, 0], [1, 2]]

np_a = np.array(a)
np_b = np.array(b)

print('-> First matrix')
print(np_a)

print('-> Second Matrix')
print(np_b)

print('-> Addition')
add = np_a + np_b
print(add)

print('-> Subtraction')
sub = np_a - np_b
print(sub)

print('-> Element wise Multiplication')
mul0 = np_a * np_b
print(mul0)

print('-> Multiplication')
mul1 = np_a.dot(np_b)
print(mul1)
