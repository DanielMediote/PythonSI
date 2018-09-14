import sqlite3

class BancoDeDados:
    def __init__(self, nome = 'banco.db'):
        self.nome, self.conexao = nome, None

    def conecta(self):
        self.conexao = sqlite3.connect(self.nome)

    def deconecta(self):
        try:
            self.conexao.close()
        except AttributeError:
            pass
