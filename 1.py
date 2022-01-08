# import numpy

# arr = numpy.array([1, 2, 3, 4, 5])

# print(arr)

import numpy as np
# print(np.__version__)
a = np.array([1, 2, 3, 4, 5, 6, 7])
b = np.array([1, 2, 3, 4], ndmin=5)
# b = np.array((1, 2, 3, 4, 5))
c = np.array(42)
d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
e = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
f = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
g = np.array(['apple', 'banana', 'cherry'])
h = np.array([1, 2, 3, 4], dtype='S')
i = np.array([1, 2, 3, 4], dtype='i4')
j = np.array([1.1, 2.1, 3.1])
k = np.array([1, 2, 3, 4, 5, 4, 4])
l = np.array([3, 2, 0, 1])
m = np.array([1, 0, 3])
n = np.array([1, 2, 3, 4, 5, 6, 7, 8])
o = np.array([1, 2, 3])
p = np.array([[1, 2, 3], [4, 5, 6]])
q = np.array([4, 5, 6])
r = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
s = np.array(['banana', 'cherry', 'apple'])
t = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
])
u = np.array([True, False, True])
v = np.array([6, 7, 8, 9])
w = np.array([[3, 2, 4], [5, 0, 1]])
x = np.array([41, 42, 43, 44])
y = np.array([1, 3, 5, 7])

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

# b = a.copy()
# a[0] = 42
# print(a)
# print(b)

# f = a.view()
# print(f)
# f[0] = 31
# print(f)

# print(b.base)
# print(f.base)

# print(d.shape)
# print(b)
# print('shape of array :', b.shape)

# k = f.reshape(4, 3)
# print(k)

# l = f.reshape(2, 3, 2)
# print(l)

# print(n.reshape(2, 4).base)

# o = n.reshape(2, 2, -1)
# print(o)

# q = p.reshape(-1)
# print(q)

# for x in a:
#     print(x)

# for x in d:
#     print(x)

# for x in d:
#     for y in x:
#         print(y)

# for x in e:
#     print(x)

# for x in e:
#     for y in x:
#         for z in y:
#             print(z)

# for x in np.nditer(e):
#     print(x)

# for x in np.nditer(a, flags=['buffered'], op_dtypes=['S']):
#     print(x)

# for idx, x in np.ndenumerate(a):
#     print(idx, x)

# for idx, x in np.ndenumerate(d):
#     print(idx, x)

# k = np.concatenate((a, n))
# print(k)

# l = np.concatenate((d, p), axis=1)
# print(l)

# r = np.stack((o, q), axis=1)
# print(r)

# s = np.hstack((o, q))
# print(s)

# t = np.vstack((o, q))
# print(t)

# u = np.dstack((o, q))
# print(u)

# k = np.array_split(a, 3)
# print(k)

# l = np.array_split(a, 4)
# print(l)

# print(k[0])
# print(k[1])
# print(k[2])

# s = np.array_split(r, 3)
# print(s)

# u = np.array_split(t, 3)
# print(u)

# v = np.array_split(t, 3, axis=1)
# print(v)

# w = np.hsplit(t, 3)
# print(w)

# l = np.where(k == 4)
# print(l)

# s = np.where(a%2 == 0)
# print(s)

# u = np.where(a%2 == 1)
# print(u)

# w = np.searchsorted(v, 7)
# print(w)

# x = np.searchsorted(v, 7, side='right')
# print(x)

# y = np.searchsorted(v, [2, 4, 6])
# print(y)

print(np.sort(l))
print(np.sort(s))
print(np.sort(u))
print(np.sort(w))

z = []

for element in x:
    if element > 42:
        z.append(True)
    else:
        z.append(False)

aa = x[z]

print(z)
print(aa)


ab = []

for element in a:
    if element % 2 == 0:
        ab.append(True)
    else:
        ab.append(False)
    
ac = a[ab]

print(ab)
print(ac)

ad = x > 42
ae = x[ad]
print(ad)
print(ae)

af = a % 2 == 0
ag = a[af]
print(af)
print(ag)