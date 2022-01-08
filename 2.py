from numpy import random

a = random.randint(100)
print(a)

b = random.rand()
print(b)

c = random.randint(100, size=(5))
print(c)

d = random.randint(100, size=(3, 5))
print(d)

e = random.rand(5)
print(e)

f = random.rand(3, 5)
print(f)

g = random.choice([3, 5, 7, 9])
print(g)

h = random.choice([3, 5, 7, 9], size=(3, 5))