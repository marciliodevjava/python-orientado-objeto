from datetime import datetime
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construinfo objeto ... {}".format(self))
        self.__numero = int(numero)
        self.__titular = str(titular)
        self.__saldo = float(saldo)
        self.__limite = float(limite)
        self.__data = self.formata_data()

    def saca(self, valor):
        if self.__saldo >= float(valor):
            self.__saldo -= float(valor)
            return "Saque realiado de R$:{}".format(float(valor))

        return "Seu Saldo é {}".format(float(self.__saldo))

    def deposita(self, valor):
        self.__saldo += float(valor)
        return "Seu Saldo é R$:{}".format(float(self.__saldo))

    def extrato(self):
        print("Nome: {}".format(self.__titular))
        print("Saldo R$:{}".format(float(self.__saldo)))
        print("Limite de credito R$:{}".format(float(self.__limite)))
        print("Data de Abertura de conta {}".format(self.__data))

    def transferir(self, conta, valor):
        if self.__saldo >= float(valor):
            self.__saldo -= float(valor)
            conta.__saldo += float(valor)
            return "Transferencia Realidade de R$:{}".format(float(valor))

        return "Saldo insuficiente R$:{}".format(float(self.__saldo))

    def formata_data(self):
        data_atual = datetime.now()
        data_formatada = data_atual.strftime("%m-%d-%Y")
        return data_formatada