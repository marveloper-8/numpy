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
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.distplot([0, 1, 2, 3, 4, 5])
# plt.show()

from numpy import random
# a = random.normal(size=(2, 3))
# print(a)

# b = random.normal(loc=1, scale=2, size=(2, 3))
# print(b)

# a = random.binomial(n=10, p=0.5, size=10)
# print(a)

# a = random.poisson(lam=2, size=10)
# print(a)

# a = random.uniform(size=(2, 3))
# print(a)

# a = random.logistic(loc=1, scale=2, size=(2, 3))
# print(a)

# a = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
# print(a)

# a = random.exponential(scale=2, size=(2,3))
# print(a)

# a = random.chisquare(df=2, size=(2, 3))
# print(a)

# a = random.rayleigh(scale=2, size=(2, 3))
# print(a)

# a = random.pareto(a=2, size=(2, 3))
# print(a)

# a = random.zipf(a=2, size=(2, 3))
# print(a)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

a = random.zipf(a=2, size=1000)
sns.distplot(a[a<10], kde=False)

plt.show()

# sns.distplot(random.pareto(a=2, size=1000), kde=False)

# sns.distplot(random.rayleigh(size=1000), hist=False)

# sns.distplot(random.chisquare(df=1, size=1000), hist=False)

# sns.distplot(random.exponential(size=1000), hist=False)

# sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
# sns.distplot(random.logistic(size=1000), hist=False, label='logistic')

# sns.distplot(random.logistic(size=1000), hist=False)

# sns.distplot(random.uniform(size=1000), hist=False)

# sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
# sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')

# sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
# sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')

# sns.distplot(random.poisson(lam=2, size=1000), kde=False)

# sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
# sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')

# plt.show()

# sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)

# plt.show()