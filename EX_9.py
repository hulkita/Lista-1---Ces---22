import sys

def is_palindrome(palavra):
    for i in range(0, len(palavra)):
        if palavra[i] != palavra[len(palavra) - i - 1]:
            return False
    return True

def test(did_pass):
    linha = sys._getframe(1).f_lineno
    if did_pass:
        msg = ("Test at line {0} ok.".format(linha))
    else:
        msg = ("Test at line {0} FAILED.".format(linha))
    print(msg)

def test_suite():
    test(is_palindrome("abba"))
    test(is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(is_palindrome("natan"))
    test(is_palindrome("teste"))


test_suite()