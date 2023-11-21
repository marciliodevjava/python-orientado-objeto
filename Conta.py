class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construinfo objeto ... {}".format(self))
        self.__numero = int(numero)
        self.__titular = str(titular)
        self.__saldo = float(saldo)
        self.__limite = float(limite)

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
            conta.__saldo += valor
            return "Transferencia Realidade de R$:{}".format(float(valor))

        return "Saldo insuficiente R$:{}".format(float(self.__saldo))
