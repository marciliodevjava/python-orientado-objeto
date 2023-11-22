
class Cliente:

    def __init__(self, nome, cpf, rg, email):
        self.__nome = self.formata_nome(nome)
        self.__cpf = int(cpf)
        self.__rg = int(rg)
        self.__email = str(email)

    def informacoes(self):
        print(f"Nome: {self.__nome}")
        print(f"Cpf: {self.__cpf}")
        print(f"Rg: {self.__rg}")
        print(f"Email: {self.__email}")

    def formata_nome(self, nome):
        self.__nome = nome.title()
        return self.__nome

    @property
    def get_nome(self):
        return self.__nome
