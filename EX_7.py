import sys

def sum_of_squares(lista):
    soma = 0
    if len(lista) > 0:
        for n in range(0, len(lista)):
            a = lista[n]
            soma += a * a
        print(f'A soma dos quadrados é {soma}')
        return soma
    else:
        return 1


def test(did_pass):
    linha = sys._getframe(1).f_lineno
    if did_pass:
        msg = ("Test at line {0} ok.".format(linha))
    else:
        msg = ("Test at line {0} FAILED.".format(linha))
    print(msg)

def test_suite():
    test(sum_of_squares([2, 3, 4]) == 29)
    test(sum_of_squares([-1, -2, 0]) == 5)
    test(sum_of_squares([0]) == 0)
    test(sum_of_squares([]) == 0)
    test(sum_of_squares([2, -3, 4]) == 29)
    test(sum_of_squares([1]) == 1)

test_suite()