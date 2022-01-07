# import numpy

# arr = numpy.array([1, 2, 3, 4, 5])

# print(arr)

import numpy as np
# print(np.__version__)
a = np.array([1, 2, 3, 4, 5])
print(a)
print(type(a))

b = np.array((1, 2, 3, 4, 5))
print(b)

c = np.array(42)
print(c)

d = np.array([[1, 2, 3], [4, 5, 6]])
print(d)

e = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(e)

print(c.ndim)
print(b.ndim)
print(d.ndim)
print(e.ndim)

f = np.array([1, 2, 3, 4], ndmin=5)
print(f)
print('number of dimensions: ', f.ndim)