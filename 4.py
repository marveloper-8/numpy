import pandas as pd

a = {
    'cars': ['BMW', 'Volvo', 'Ford'],
    'passings': [3, 7, 2]
}
b = pd.DataFrame(a)
print(b)