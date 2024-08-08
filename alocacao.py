class Alocacao(Funcionario, Projeto):
    def init(self, nome_funcionario, codigo_projeto, data_inicio_alocacao):
        super().init()
        super().init()
        self.nome_funcionario = nome_funcionario
        self.codigo_projeto = codigo_projeto
        self.data_inicio_alocacao = data_inicio_alocacao

    def descrever_alocacao(self):
        return f"Alocação para o funcionário {self.nome_funcionario} no projeto {self.codigo_projeto} iniciada em {self.data_inicio_alocacao}"