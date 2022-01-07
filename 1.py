# import numpy

# arr = numpy.array([1, 2, 3, 4, 5])

# print(arr)

import numpy as np
# print(np.__version__)
a = np.array([1, 2, 3, 4, 5, 6, 7])
# print(a)
# print(type(a))

# b = np.array((1, 2, 3, 4, 5))
# print(b)

c = np.array(42)
# print(c)

d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(d)

e = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(e)

# print(c.ndim)
# print(b.ndim)
# print(d.ndim)
# print(e.ndim)

# f = np.array([1, 2, 3, 4], ndmin=5)
# print(f)
# print('number of dimensions: ', f.ndim)

f = np.array([1, 2, 3, 4])
print(f[0])
print(f[1])
print(f[2] + f[3])

print('2nd element on 1st row: ', d[0, 1])
print('5th element on 2nd row: ', d[1, 4])
print(e[0, 1, 2])
print('Last element from 2nd dim: ', d[1, -1])