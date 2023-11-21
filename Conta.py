class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construinfo objeto ... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def saca(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return "Saque realiado de R$:{}".format(float(valor))

        return "Seu Saldo é {}".format(float(self.saldo))

    def deposita(self, valor):
        self.saldo += valor
        return "Seu Saldo é R$:{}".format(float(self.saldo))

    def extrato(self):
        print("Nome: {}".format(self.titular))
        print("Saldo R$:{}".format(float(self.saldo)))
        print("Limite de credito R$:{}".format(float(self.limite)))

    def transferir(self, conta, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            conta.saldo += valor
            return "Transferencia Realidade de R$:{}".format(float(valor))

        return "Saldo insuficiente R$:{}".format(float(self.saldo))
