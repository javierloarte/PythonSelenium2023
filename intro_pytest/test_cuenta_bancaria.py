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
        pass


## *******************************************************
## Validacion
## *******************************************************

    @classmethod
    def setup_class(cls):
        print("*" * 80)
        print(f"CLASS SETUP - Crear usuario con la llamada a la BD")
        print("*" * 80)

    def test_cuentaBancaria():
        print("test cuenta bancaria")

    @classmethod
    def teardown_class(cls):
        print("*" * 80)
        print(f"TEARDOWN SETUP - limpiar usuario con la llamada a la BD")
        print("*" * 80)
