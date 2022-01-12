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
print(b[0])

c = pd.Series(a, index=["x", "y", "z"])
print(c)