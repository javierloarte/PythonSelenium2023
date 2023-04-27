
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

#*******************************************************
# Validacion
# *******************************************************
def test_cuentaBancaria():
    print("test cuenta bancaria")
