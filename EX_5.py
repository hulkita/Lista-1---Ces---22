def sum_until_sam(lista):
    soma = 0
    for i in lista:
        if(i == 'sam'):
            return soma + 1
        soma = soma + 1
    print("There is no 'sam' ")
    return soma

lista = ["csgo", "carro", "matheus", "queijo", "sam"]


print(sum_until_sam(lista))