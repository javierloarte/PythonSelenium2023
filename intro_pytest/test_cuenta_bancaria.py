import pytest

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad


    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("No tienes suficiente saldo")
        self.saldo -= cantidad

    def consultar_saldo(self):
        return self.saldo

## *******************************************************
## Validacion
## *******************************************************

class Test_CuentaBancaria:

    @classmethod
    def setup_class(cls):
        print("*" * 80)
        print(f"CLASS SETUP - Crear usuario con la llamada a la BD")
        print("*" * 80)
    def setup_method(self):
        print("*" * 80)
        print(f"METHOD SETUP - Abrir un nuevo navegador")
        print("*" * 80)
        self.cuenta = CuentaBancaria("Pedro", 100)
        print(self.cuenta.titular)
        print(self.cuenta.saldo)

    def test_depositar(self):
        self.cuenta.depositar(20)
        assert self.cuenta.consultar_saldo() == 120, "Prueba Incorrecta"
        print(self.cuenta.saldo)

    def test_retirar(self):
        self.cuenta.retirar(40)
        assert self.cuenta.consultar_saldo() == 60, "Prueba Incorrecta"

    def teardown_method(self):
        print("*" * 80)
        print(f"TEARDOWN SETUP - Cerrar el navegador")
        print("*" * 80)

    @classmethod
    def teardown_class(cls):
        print("*" * 80)
        print(f"TEARDOWN SETUP - limpiar usuario con la llamada a la BD")
        print("*" * 80)
