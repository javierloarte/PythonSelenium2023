
def es_par(num_a: int, num_b: int) -> bool:
    return num_a % 2 == 0 and num_b % 2 == 0:
        return True
    else:
        return False


def test_positive():
    result = es_par(4, 2)
    assert result, "La funcion es par debe ser verdadero 4 , 2"

def test_negativo():
    result = es_par(4, 3)
    assert result, "el numero no es par"