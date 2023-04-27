import pytest

class Calculadora:
    def __init__(self):
        pass

def suma(self, num_a: int, num_b: int):
    return num_a + num_b

def resta(self, num_a: int, num_b: int):
    return num_a + num_b

def multiplicacion(self, num_a: int, num_b: int):
    return num_a ** num_b

def division(self, num_a: int, num_b: int):
    return num_a // num_b


def test_suma_valid_input():
    calc = Calculadora()
    result = calc.suma(2, 2)
    assert result == 2, "el resultado es 5"

def test_restar():
    result = resta("ok",2, 10)
    assert result, "La resta es incorrecta"


def test_multiplica():
    result = resta("ok",2, 10)
    assert result, "La multiplicacion es incorrecta"


def test_division():
    result = resta("ok",2, 10)
    assert result, "La division es incorrecta"


def test_sumando():
    assert suma("ok",10, 3) == 12, "La suma es incorrecta"

def test_restando():
    assert resta("ok",9, 3) == 4, "La resta es incorrecta"

def test_multiplicando():
    assert resta("ok",9, 2) == 20, "La muliplicacion es incorrecta"

def test_dividiendo():
    assert resta("ok",9, 3) == 2, "La division es incorrecta"