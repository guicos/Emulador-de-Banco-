
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo obj...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    def extrato(self):
        print(f"O seu saldo é {self.__saldo}")

    def depositado(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transferencia(self, valor, destino):
        self.saca(valor)
        destino.depositado(valor)

    @property
    def limite(self):
        return self.__limite

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
