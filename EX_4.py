def sum_until_par(lista):
    soma = 0
    for i in lista:
        print(i)
        if((i % 2 )== 0):
            return soma
        soma = soma + i
    print("There is no even number")
    return soma

lista = [1, 21, 35, 40, 50]
lista.append(60)

print(sum_until_par(lista))