from funcionario import Funcionario
from projeto import Projeto

class Alocacao:
    def __init__(self, funcionario, projeto, data_inicio_alocacao):
        self.__funcionario = funcionario
        self.__projeto = projeto
        self.__data_inicio_alocacao = data_inicio_alocacao

    def get_funcionario(self):
        return self.__funcionario

    def get_projeto(self):
        return self.__projeto

    def get_data_inicio_alocacao(self):
        return self.__data_inicio_alocacao

    def set_funcionario(self, funcionario):
        self.__funcionario = funcionario

    def set_projeto(self, projeto):
        self.__projeto = projeto

    def set_data_inicio_alocacao(self, data_inicio_alocacao):
        self.__data_inicio_alocacao = data_inicio_alocacao

    def descrever_alocacao(self):
        return (f'Alocação para o funcionário {self.__funcionario.get_nome()} no projeto '
                f'"{self.__projeto.get_nome()}" iniciada em {self.__data_inicio_alocacao}')
