from model import model

class control:

    def __init__(self):
        self.opcao = -1
        self.modelo = model()

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def menu(self):
        print("Escolha uma das opções abaixo: \n"      +
              "0.Sair\n"                               +
              "1.Cadastrar\n"                          +
              "2.Consultar\n"                          +
              "3.Atualizar Nome\n"                     +
              "4.Atualizar Telefone\n"                 +
              "5.Atualizar Endereço\n"                 +
              "6.Atualizar Data de Nascimento\n"       +
              "7.Excluir")
        self.setOpcao(int(input()))

    def operacoes(self):

        while self.getOpcao() != 0:
            self.menu()
            if self.getOpcao() == 0:
                print("OBRIGADA!")
            elif self.getOpcao() == 1:
                self.cadastrar()
            elif self.getOpcao() == 2:
                print(self.modelo.selecionar())
            elif self.getOpcao() == 3:
                self.atualizarNome()
            elif self.getOpcao() == 4:
                self.atualizarTelefone()
            elif self.getOpcao() == 5:
                self.atualizarEndereco()
            elif self.getOpcao() == 6:
                self.atualizarDataDeNascimento()
            elif self.getOpcao() == 7:
                self.excluir()
            else:
                print("Opcão escolhida não é valida! Tente novamente!")






    def cadastrar(self):
        print("Informe seu nome: ")
        nome = input()
        print("Informe seu telefone: ")
        telefone = input()
        print("Informe seu endereco: ")
        endereco = input()
        print("Informe sua data de nascimento:")
        dataDeNascimento = input()
        print(self.modelo.inserir(nome, telefone, endereco, self.transformarData(dataDeNascimento)))

    def transformarData(self, texto):
        separado = texto.split('/')
        dia = separado[0]
        mes = separado[1]
        ano = separado[2]
        return "{}-{}-{}".format(ano, mes, dia)

    def atualizarNome(self):
        print("Informe o código do dado que será atualizado")
        codigo = int(input())
        print("Informe o novo nome")
        name = input()
        print(self.modelo.atualizar("nome", name, codigo))

    def atualizarTelefone(self):
        print("Informe o código do dado que será atualizado")
        codigo = int(input())
        print("Informe o novo telefone")
        telefono = input()
        print(self.modelo.atualizar("telefone", telefono, codigo))

    def atualizarEndereco(self):
        print("Informe o código do dado que será atualizado")
        codigo = int(input())
        print("Informe o novo telefone")
        endere = input()
        print(self.modelo.atualizar("endereco", endere, codigo))

    def atualizarDataDeNascimento(self):
        print("Informe o código do dado que será atualizado")
        codigo = int(input())
        print("Informe o nova Data de Nascimento")
        nascime = self.transformarData(input())
        print(self.modelo.atualizar("dataDeNascimento", nascime, codigo))

    def excluir(self):
        print("Informe o código do daod que deseja excluir: ")
        cod = int(input())
        print(self.modelo.excluir(cod))