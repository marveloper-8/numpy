# import pandas as pd

# a = {
#     'cars': ['BMW', 'Volvo', 'Ford'],
#     'passings': [3, 7, 2]
# }
# b = pd.DataFrame(a)
# print(b)

# print(pd.__version__)

import pandas as pd
a = [1, 7, 2]
b = pd.Series(a)
print(b)
print(b[0])

c = pd.Series(a, index=["x", "y", "z"])
print(c)
print(c["y"])

d = {
    "day1": 420,
    "day2": 380,
    "day3": 390
}
e = pd.Series(d)
print(e)