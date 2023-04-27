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
calc = Calculadora()

def test_suma_valores():
    assert calc.suma( 10, 3) == 13, "La suma es incorrecta"

def test_resta_valores():
    assert calc.resta( 9, 3) == 6, "La resta es incorrecta"

def test_multiplica_valores():
    assert calc.multiplicacion( 9, 2) == 18, "La muliplicacion es incorrecta"

def test_divide_valores():
    assert calc.division( 12, 3) == 4, "La division es incorrecta"