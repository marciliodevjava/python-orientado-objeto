class Conta:

    def __init__(self, numero:int, titular:str, saldo:float, limite:float):
        print("Construinfo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def saca(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return "Saque realiado de R$:{}".format(float(valor))

        return "Seu Saldo é {}".format(float(self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor
        return "Seu Saldo é R$:{}".format(float(self.__saldo))

    def extrato(self):
        print("Nome: {}".format(self.__titular))
        print("Saldo R$:{}".format(float(self.__saldo)))
        print("Limite de credito R$:{}".format(float(self.__limite)))

    def transferir(self, conta, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            conta.saldo += valor
            return "Transferencia Realidade de R$:{}".format(float(valor))

        return "Saldo insuficiente R$:{}".format(float(self.__saldo))
