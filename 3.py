import numpy as np

#normal python ufunc
a = [1, 2, 3, 4]
b = [4, 5, 6, 7]
c = []

for i, j in zip(a, b):
    c.append(i + j)
print(c)

#numpy ufunc
d = np.add(a, b)
print(d)

#custom numpy ufunc
def myadd(e, f):
    return e + f

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

print(type(np.add))
print(type(np.concatenate))

if type(np.add) == np.ufunc:
    print('add is ufunc')
else:
    print('add is not ufunc')