from Conta import Conta


class TestConta:
    separado = "============================================"
    conta = Conta(12, 12, "Marcilio", 100, 1000)
    conta.extrato()
    print(separado)
    conta.saca(800)
    conta.extrato()
    print(separado)
    conta.deposita(1000)
    conta.extrato()
    print(separado)
    conta.pagar_conta()
    conta.extrato()
    print(separado)
    conta.fechar_conta()
    conta.extrato()