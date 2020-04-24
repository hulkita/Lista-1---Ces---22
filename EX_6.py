import sys
from random import randint

def is_prime(n):
    if n > 1:
        for i in range(2, n//2):
            if(n % i) == 0:
                print(f'O numero {n} nao é primo')
                return False
        print(f'O numero {n} é primo')
        return True
    else:
        print(f'O numero {n} precisa ser maior que 1 para ser primo')
    return False

def test(did_pass):
    linha = sys._getframe(1).f_lineno
    if did_pass:
        msg = ("Test at line {0} ok.".format(linha))
    else:
        msg = ("Test at line {0} FAILED.".format(linha))
    print(msg)

def test_suite():
    test(is_prime(11))
    test(is_prime(135))
    test(is_prime(19911121))
    test(is_prime(47))
    test(is_prime(2))
    test(is_prime(-5))
    test(is_prime(31)) #My birth date
    test(is_prime(13))
    test(not is_prime(6))

def teste_100_pessoas():
    print(f'Vamos realizar uma simulaçao de 100 numeros aleatorios\n'
          f'entre 1 e 31 referente a data de aniversario de pessoas\n'
          f'para saber quantas nasceram em dias primos. \n')
    primos = 0
    for data in range(1, 100):
        numero_aleatorio = randint(1, 31)
        if is_prime(numero_aleatorio):
            primos += 1
    print(f'Dos 100 numeros simulados:'
          f'{primos} sao primos')
test_suite()
teste_100_pessoas()


