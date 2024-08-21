class Projeto:
    def __init__(self, codigo, nome, data_inicio):
        self.__codigo = codigo
        self.__nome = nome
        self.__data_inicio = data_inicio

    def get_codigo(self):
        return self.__codigo

    def get_nome(self):
        return self.__nome

    def get_data_inicio(self):
        return self.__data_inicio

    def set_nome(self, nome):
        self.__nome = nome

    def set_data_inicio(self, data_inicio):
        self.__data_inicio = data_inicio

    def descrever_projeto(self):
        return (f'O código {self.__codigo} do projeto "{self.__nome}", tem a data de início '
                f'{self.__data_inicio}')
