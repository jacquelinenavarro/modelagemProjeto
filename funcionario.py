class Funcionario:
    def __init__(self, id, nome, cargo, genero):
        self.id = id
        self.nome = nome
        self.cargo = cargo
        self.genero = genero

    def descrever_funcionario(self):
        return f"Funcionario(id={self.id}, nome={self.nome}, cargo={self.cargo}, genero={self.genero})"
