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


## ///////////////////////////////////////////////////////////////////////
## Validacion
## ///////////////////////////////////////////////////////////////////////

def test_sumando():
    calc = Calculadora()
    assert calc.suma( 10, 3) == 13, "La suma es incorrecta"

def test_restando():
    assert resta( 9, 3) == 4, "La resta es incorrecta"

def test_multiplicando():
    assert resta( 9, 2) == 20, "La muliplicacion es incorrecta"

def test_dividiendo():
    assert resta( 9, 3) == 2, "La division es incorrecta"