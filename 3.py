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

# a = np.arange(1, 10)
# print(np.log2(a))

# b = np.arange(1, 10)
# print(np.log10(b))

# c = np.arange(1, 10)
# print(np.log(c))

# d = np.frompyfunc(log, 2, 1)
# print(d(100, 15))

# a = np.array([1, 2, 3])
# b = np.array([1, 2, 3])

# c = np.add(a, b)
# print(c)

# d = np.sum([a, b])
# print(d)

# e = np.sum([a, b], axis=1)
# print(e)

# f = np.cumsum(a)
# print(f)

# from math import log
# import numpy as np

# a = np.array([1, 2, 3, 4])
# c = np.array([5, 6, 7, 8])

# b = np.prod(a)
# print(b)

# d = np.prod([a, c])
# print(d)

# e = np.prod([a, c], axis=1)
# print(e)

# f = np.cumprod(c)
# print(f)

# import numpy as np

# a = np.array([10, 15, 25, 5])
# b = np.diff(a)
# print(b)

# c = np.diff(a, n=2)
# print(c)

# import numpy as np

# a, b = 4, 6
# c = np.lcm(a, b)
# print(c)

# d = np.array([3, 6, 9])
# e = np.lcm.reduce(d)
# print(e)

# f = np.arange(1, 11)
# g = np.lcm.reduce(f)
# print(g)

# import numpy as np

# a = 6
# b = 9

# c = np.gcd(a, b)
# print(c)

# d = np.array([20, 8, 32, 36, 16])
# e = np.gcd.reduce(d)
# print(e)

# import numpy as np

# a = np.sin(np.pi/2)
# print(a)

# b = np.array([
#     np.pi/2,
#     np.pi/3,
#     np.pi/4,
#     np.pi/5
# ])
# c = np.sin(b)
# print(c)

# d = np.array([90, 180, 270, 360])
# e = np.deg2rad(d)
# print(e)

# f = np.array([
#     np.pi/2,
#     np.pi,
#     1.5*np.pi,
#     2*np.pi
# ])
# g = np.rad2deg(f)
# print(g)

# h = np.arcsin(1.0)
# print(h)

# i = np.array([1, -1, 0.1])
# j = np.arcsin(i)
# print(j)

# k = 3
# l = 4
# m = np.hypot(k, l)
# print(m)

import numpy as np

a = np.sinh(np.pi/2)
print(a)

b = np.array([
    np.pi/2,
    np.pi/3,
    np.pi/4,
    np.pi/5
])
c = np.cosh(b)
print(c)

d = np.arcsinh(1.0)
print(d)