from datetime import datetime


class Conta:

    def __init__(self, numero, agencia, titular, saldo, limite):
        print("Construinfo objeto ... {}".format(self))
        self.__numero = int(numero)
        self.__agencia = int(agencia)
        self.__titular = str(titular)
        self.__saldo = float(saldo)
        self.__limite = float(limite)
        self.__data = self.__formata_data()
        self.__valor_devido = float(0.0)
        self.__valor_limite = self.__limite
        self.__codigo_banco = "001"
        self.__conta_fechada = False

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = str(titular)

    def get_agencia(self):
        return self.__agencia

    def get_numero(self):
        return self.__numero

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = float(limite)

    def get_data(self):
        return self.__data

    def saca(self, valor):
        valor_conta = self.__limite + self.__saldo
        if self.__saldo >= float(valor):
            self.__saldo -= float(valor)
            return "Saque realiado de R$:{}".format(float(valor))
        elif valor_conta >= float(valor):
            valor_restante = valor - self.__saldo
            self.__saldo = 0
            self.__limite -= valor_restante
            self.__valor_devido = valor_restante
            return "Saque realiado de R$:{}".format(float(valor))
        return "Seu Saldo é {}".format(float(self.__saldo))

    def deposita(self, valor):
        self.__saldo += float(valor)
        return "Seu Saldo é R$:{}".format(float(self.__saldo))

    def extrato(self):
        print("Número: {}".format(self.__numero))
        print("Agencia: {}".format(self.__agencia))
        print("Nome: {}".format(self.__titular))
        print("Saldo R$:{}".format(float(self.__saldo)))
        print("Limite de credito R$:{}".format(float(self.__limite)))
        print(("Valor devido R$: {}".format(self.__valor_devido)))
        print("Codigo do Banco do Brasil {}".format(self.__codigo_banco))
        print("Data de Abertura de conta {}".format(self.__data))

    def transferir(self, conta, valor):
        if self.__saldo >= float(valor):
            self.__saldo -= float(valor)
            conta.__saldo += float(valor)
            return "Transferencia Realidade de R$:{}".format(float(valor))

        return "Saldo insuficiente R$:{}".format(float(self.__saldo))

    def __formata_data(self):
        data_atual = datetime.now()
        data_formatada = data_atual.strftime("%m-%d-%Y")
        return data_formatada

    def fechar_conta(self):
        if self.validar_conta_fechar():
            print("Fechando a conta.")
            self.__numero = None
            self.__titular = None
            self.__saldo = float(0.0)
            self.__limite = float(0.0)
            self.__agencia = None
            self.__conta_fechada = True
            self.__valor_devido = float(0.0)
            self.__data = self.__formata_data()
            print("Conta fechada com sucesso.")
        else:
            return "Nã foi possivel fechar a conta, pois á Saldo R$: {} ou Débitos R$: {}".format(self.__saldo,
                                                                                                  self.__valor_devido)

    def validar_conta_fechar(self):
        if self.__saldo == 0 and self.__valor_devido == 0:
            return True

    def pagar_conta(self):
        if self.__saldo >= 1 and self.__valor_devido > 0:
            valor_pago = float(0)
            valor_devido = self.__valor_devido
            valor_saldo = self.__saldo
            if self.__saldo <= self.__valor_devido:
                self.__saldo = float(0.0)
                self.__valor_devido -= self.__saldo
                self.__limite += self.saldo
                valor_pago = valor_devido - self.__valor_devido
            else:
                self.__saldo -= valor_devido
                self.__limite = self.__valor_limite
                self.__valor_devido = float(0)
                valor_pago = valor_devido - self.__valor_devido
            return "Conta paga com sucesso R$: {}".format(float(valor_pago))
        elif self.__valor_devido <= 0:
            return "Não existe valores a serem pagos"
        else:
            return "Não foi possivel pagar a conta"

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_dos_bancos():
        return {'Banco do Brasil': '001', 'Caixa Economica': '104', 'Bradesco': '237'}
