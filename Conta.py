

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construinfo objeto ... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def sacar(self, conta, valor):
        if conta.saldo >= valor:
            self.saldo -= valor
            return "Saque realiado de R$:{}".format(float(valor))

        return "Seu Saldo é {}".format(float(conta.saldo))
