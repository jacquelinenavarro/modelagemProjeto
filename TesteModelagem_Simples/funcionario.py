class Funcionario:
    def __init__(self, id, nome, cargo, genero):
        self.__id = id
        self.__nome = nome
        self.__cargo = cargo
        self.__genero = genero

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_cargo(self):
        return self.__cargo

    def get_genero(self):
        return self.__genero

    def set_nome(self, nome):
        self.__nome = nome

    def set_cargo(self, cargo):
        self.__cargo = cargo

    def set_genero(self, genero):
        self.__genero = genero

    def descrever_funcionario(self):
        return (f'Funcionário(id={self.__id}, nome={self.__nome}, cargo={self.__cargo}, '
                f'genero={self.__genero})')
