class Pessoa(object):
    """docstring forPessoa."""
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __rept__(self):
        return self.nome

    def pelo_nome(pessoa):
        return pessoa.nome

    def pela_idade(pessoa):
        return pessoa.idade

p1 = Pessoa("Marcelo", 28)
p2 = Pessoa("João", 36)
p3 = Pessoa("Ana", 25)
