# import numpy as np

#normal python ufunc
# a = [1, 2, 3, 4]
# b = [4, 5, 6, 7]
# c = []

# for i, j in zip(a, b):
#     c.append(i + j)
# print(c)

#numpy ufunc
# d = np.add(a, b)
# print(d)

#custom numpy ufunc
# def myadd(e, f):
#     return e + f

# myadd = np.frompyfunc(myadd, 2, 1)

# print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

# print(type(np.add))
# print(type(np.concatenate))

# if type(np.add) == np.ufunc:
#     print('add is ufunc')
# else:
#     print('add is not ufunc')

# e = np.array([10, 11, 12, 13, 14, 15])
# f = np.array([20, 21, 22, 23, 24, 25])
# g = np.array([10, 20, 30, 40, 50, 60])
# h = np.array([3, 5, 10, 8, 2, 33])
# i = np.array([3, 5, 6, 8, 2, 33])
# j = np.array([3, 7, 9, 8, 2, 33])
# n = np.array([-1, -2, 1, 2, 3, -4])

# g = np.add(e, f)
# print(g)

# h = np.subtract(g, f)
# print(h)

# i = np.multiply(g, f)
# print(i)

# i = np.divide(g, h)
# print(i)

# j = np.power(g, i)
# print(j)

# k = np.mod(g, j)
# print(k)

# l = np.remainder(g, j)
# print(l)

# m = np.divmod(g, j)
# print(m)

# o = np.absolute(n)
# print(o)

import numpy as np

# a = np.trunc([-3.1666, 3.6667])
# print(a)

# b = np.fix([-3.1666, 3.6667])
# print(b)

# c = np.around(3.1666, 2)
# print(c)

# d = np.floor([-3.1666, 3.6667])
# print(d)

# e = np.ceil([-3.1666, 3.6667])
# print(e)

a = np.arange(1, 10)
print(np.log2(a))

b = np.arange(1, 10)
print(np.log10(b))