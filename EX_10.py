def complex_addition(a, b):
    return (a[0] + b[0], a[1] + b[1])


a = (3, 2)

b = (4, -1)

print(f'A soma dos complexos {a[0]} + {a[1]}i  e  {b[0]} + {b[1]} é:')
print(f'{complex_addition(a, b)[0]} + {complex_addition(a, b)[1]}i')

