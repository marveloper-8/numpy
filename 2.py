# from numpy import random
# import numpy as np

# a = random.randint(100)
# print(a)

# b = random.rand()
# print(b)

# c = random.randint(100, size=(5))
# print(c)

# d = random.randint(100, size=(3, 5))
# print(d)

# e = random.rand(5)
# print(e)

# f = random.rand(3, 5)
# print(f)

# g = random.choice([3, 5, 7, 9])
# print(g)

# h = random.choice([3, 5, 7, 9], size=(3, 5))
# print(h)

# a = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
# print(a)

# b = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
# print(b)

# a = np.array([1, 2, 3, 4, 5])
# random.shuffle(a)
# print(a)

# print(random.permutation(a))

# import matplotlib as mpl
# mpl.use('TkAgg')
# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.distplot([0, 1, 2, 3, 4, 5])
# plt.show()

from numpy import random
# a = random.normal(size=(2, 3))
# print(a)

# b = random.normal(loc=1, scale=2, size=(2, 3))
# print(b)

# a = random.binomial(n=10, p=0.5, size=10)
# print(a)

a = random.poisson(lam=2, size=10)
print(a)