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


def test_sumatoria():
    result = suma(3,4, 2)
    assert result, "La suma es incorrecta"

def test_restar():
    result = resta("ok",2, 10)
    assert result, "La resta es incorrecta"


def test_multiplica():
    result = resta("ok",2, 10)
    assert result, "La multiplicacion es incorrecta"


def test_division():
    result = resta("ok",2, 10)
    assert result, "La division es incorrecta"