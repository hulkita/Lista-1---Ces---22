def multiplication_table(tamanho_da_tabela):
    n = tamanho_da_tabela
    print(f'   ', end="")
    for a in range(1, tamanho_da_tabela):
        if a >= 10:
            print(f'   {a}', end="")
        else:
            print(f'    {a}', end="")

    print(f'   {n}')
    print(f'  :', end="")
    for e in range(1, tamanho_da_tabela):
        print(f'-------------', end="")
    print(f'-------------')
    for b in range(1, tamanho_da_tabela + 1):
        if b >= 10:
            print(f'{b}:', end="")
        else:
            print(f' {b}:', end="")
        for a in range(1, tamanho_da_tabela + 1):
            c = a * b
            d = str(c)
            for j in range(0, 5 - len(d)):
               print(f' ', end="")
            if a == tamanho_da_tabela:
                print(f'{c}')
            else:
                print(f'{c}', end="")



multiplication_table(12)
