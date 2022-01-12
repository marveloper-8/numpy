import pandas

a = {
    'cars': ['BMW', 'Volvo', 'Ford'],
    'passings': [3, 7, 2]
}
b = pandas.DataFrame(a)
print(b)