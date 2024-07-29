class Projeto:
    def __init__(self, codigo, nome, data):
        self.codigo = codigo
        self.nome = nome
        self.data = data

    def descrever_projeto(self):
        return f'O código {self.codigo} do projeto "{self.nome}", tem a data de início {self.data}'

