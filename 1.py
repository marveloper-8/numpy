# import numpy

# arr = numpy.array([1, 2, 3, 4, 5])

# print(arr)

import numpy as np
# print(np.__version__)
a = np.array([1, 2, 3, 4, 5, 6, 7])
# b = np.array((1, 2, 3, 4, 5))
c = np.array(42)
d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
e = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
g = np.array(['apple', 'banana', 'cherry'])
h = np.array([1, 2, 3, 4], dtype='S')
i = np.array([1, 2, 3, 4], dtype='i4')
j = np.array([1.1, 2.1, 3.1])
m = np.array([1, 0, 3])

# print(a)
# print(type(a))

# print(b)

# print(c)

# print(d)

# print(e)

# print(c.ndim)
# print(b.ndim)
# print(d.ndim)
# print(e.ndim)

# f = np.array([1, 2, 3, 4], ndmin=5)
# print(f)
# print('number of dimensions: ', f.ndim)

# f = np.array([1, 2, 3, 4])
# print(f[0])
# print(f[1])
# print(f[2] + f[3])

# print('2nd element on 1st row: ', d[0, 1])
# print('5th element on 2nd row: ', d[1, 4])
# print(e[0, 1, 2])
# print('Last element from 2nd dim: ', d[1, -1])

# print(a[1:5])
# print(a[4:])
# print(a[:4])
# print(a[-3: -1])
# print(a[1:5:2])
# print(a[::2])
# print(d[1, 1:4])
# print(d[0:2, 2])
# print(d[0:2, 1:4])

# print(a.dtype)
# print(g.dtype)
# print(h)
# print(h.dtype)
# print(i)
# print(i.dtype)

# k = j.astype('i')
# print(k)
# print(k.dtype)

# l = j.astype(int)
# print(l)
# print(l.dtype)

# n = m.astype(bool)
# print(n)
# print(n.dtype)

b = a.copy()
a[0] = 42
print(a)
print(b)

f = a.view()
print(f)
f[0] = 31
print(f)

print(b.base)
print(f.base)