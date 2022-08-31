import mysql.connector
from conexao import conexao

class model:
    def __init__(self):
        self.db_connection = conexao()
        self.db_connection = self.db_connection.conectar()
        self.con = self.db_connection.cursor() #navegação no banco de dados

    def inserir(self, nome , telefone, endereco, dataDeNascimento):
        try:
            sql = "insert into pessoa(codigo, nome, telefone, endereco, dataDeNascimento) values('','{}','{}','{}','{}')".format(nome, telefone, endereco, dataDeNascimento)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linhas afetadas".format(self.con.rowcount)
        except Exception as erro:
            return erro

    def selecionar(self):
        try:
            sql = "Select * from pessoa"
            self.con.execute(sql)
            msg = ""
            for(codigo, nome, telefone, endereco, dataDeNascimento) in self.con:
                msg = msg + "\nCódigo: {}\nNome: {} \nTelefone: {} \nEndereço: {} \nData De Nascimento: {} ".format(codigo, nome, telefone, endereco, dataDeNascimento)
            return msg


        except Exception as erro:
            return erro

    def atualizar(self, campo, novoDado, cod):
        try:
            sql = "update pessoa set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha atualizada com sucesso!".format(self.con.rowcount)
        except Exception as erro:
            return erro

    def excluir(self,cod):

        try:
            sql = "delete from pessoa where codigo = '{}'".format(cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha excluida!".format(self.con.rowcount)
        except Exception as erro:
            return erro















