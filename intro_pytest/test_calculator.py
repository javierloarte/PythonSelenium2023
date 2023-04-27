import pytest

class Calculadora:
    def __init__(self):
        pass

def suma(num_a: int, num_b: int):
    return num_a + num_b

def resta(self, num_a: int, num_b: int):
    return num_a + num_b

def multiplicacion(self, num_a: int, num_b: int):
    return num_a ** num_b

def division(self, num_a: int, num_b: int):
    return num_a // num_b


def test_suma_valid_input():
    Calc = Calculadora()
    result = Calc.suma(2, 3)
    assert result == 5, "el resultado es 5"


def test_sumando():
    assert suma("ok", 10, 3) == 12, "La suma es incorrecta"

def test_restando():
    assert resta("ok", 9, 3) == 4, "La resta es incorrecta"

def test_multiplicando():
    assert resta("ok", 9, 2) == 20, "La muliplicacion es incorrecta"

def test_dividiendo():
    assert resta("ok", 9, 3) == 2, "La division es incorrecta"