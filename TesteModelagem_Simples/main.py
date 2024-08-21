from funcionario import Funcionario
from projeto import Projeto
from alocacao import Alocacao

# Armazenamento em memória para CRUD
funcionarios = []
projetos = []
alocacoes = []

def menu_principal():
    print("\nMenu Principal:")
    print("1. Gerenciar Projetos")
    print("2. Gerenciar Funcionários")
    print("3. Gerenciar Alocações")
    print("4. Sair")

def menu_crud(tipo):
    if tipo == 'projeto':
        print("\nMenu Projetos:")
        print("1. Adicionar Projeto")
        print("2. Listar Projetos")
        print("3. Atualizar Projeto")
        print("4. Remover Projeto")
    elif tipo == 'funcionario':
        print("\nMenu Funcionários:")
        print("1. Adicionar Funcionário")
        print("2. Listar Funcionários")
        print("3. Atualizar Funcionário")
        print("4. Remover Funcionário")
    elif tipo == 'alocacao':
        print("\nMenu Alocações:")
        print("1. Adicionar Alocação")
        print("2. Listar Alocações")
        print("3. Atualizar Alocação")
        print("4. Remover Alocação")
    print("5. Voltar ao Menu Principal")

def adicionar_funcionario():
    id = int(input("Digite o ID do funcionário: "))
    nome = input("Digite o nome do funcionário: ")
    cargo = input("Digite o cargo do funcionário: ")
    genero = input("Digite o gênero do funcionário: ")
    funcionario = Funcionario(id, nome, cargo, genero)
    funcionarios.append(funcionario)
    print("Funcionário adicionado com sucesso.")

def adicionar_projeto():
    codigo = int(input("Digite o código do projeto: "))
    nome = input("Digite o nome do projeto: ")
    data_inicio = input("Digite a data de início do projeto (YYYY-MM-DD): ")
    projeto = Projeto(codigo, nome, data_inicio)
    projetos.append(projeto)
    print("Projeto adicionado com sucesso.")

def adicionar_alocacao():
    id_funcionario = int(input("Digite o ID do funcionário para alocação: "))
    projeto_codigo = int(input("Digite o código do projeto para alocação: "))
    data_inicio_alocacao = input("Digite a data de início da alocação (YYYY-MM-DD): ")

    funcionario = next((f for f in funcionarios if f.get_id() == id_funcionario), None)
    projeto = next((p for p in projetos if p.get_codigo() == projeto_codigo), None)

    if funcionario and projeto:
        alocacao = Alocacao(funcionario, projeto, data_inicio_alocacao)
        alocacoes.append(alocacao)
        print("Alocação adicionada com sucesso.")
    else:
        print("Funcionário ou projeto não encontrados.")

def listar_funcionarios():
    for f in funcionarios:
        print(f.descrever_funcionario())

def listar_projetos():
    for p in projetos:
        print(p.descrever_projeto())

def listar_alocacoes():
    for a in alocacoes:
        print(a.descrever_alocacao())

def atualizar_funcionario():
    id = int(input("Digite o ID do funcionário que deseja atualizar: "))
    funcionario = next((f for f in funcionarios if f.get_id() == id), None)

    if funcionario:
        nome = input("Digite o novo nome do funcionário: ")
        cargo = input("Digite o novo cargo do funcionário: ")
        genero = input("Digite o novo gênero do funcionário: ")
        funcionario.set_nome(nome)
        funcionario.set_cargo(cargo)
        funcionario.set_genero(genero)
        print("Funcionário atualizado com sucesso.")
    else:
        print("Funcionário não encontrado.")

def atualizar_projeto():
    codigo = int(input("Digite o código do projeto que deseja atualizar: "))
    projeto = next((p for p in projetos if p.get_codigo() == codigo), None)

    if projeto:
        nome = input("Digite o novo nome do projeto: ")
        data_inicio = input("Digite a nova data de início do projeto (YYYY-MM-DD): ")
        projeto.set_nome(nome)
        projeto.set_data_inicio(data_inicio)
        print("Projeto atualizado com sucesso.")
    else:
        print("Projeto não encontrado.")

def atualizar_alocacao():
    id_funcionario = int(input("Digite o ID do funcionário da alocação que deseja atualizar: "))
    projeto_codigo = int(input("Digite o código do projeto da alocação que deseja atualizar: "))
    data_inicio_alocacao = input("Digite a nova data de início da alocação (YYYY-MM-DD): ")

    alocacao = next((a for a in alocacoes if a.get_funcionario().get_id() == id_funcionario and a.get_projeto().get_codigo() == projeto_codigo), None)

    if alocacao:
        funcionario = next((f for f in funcionarios if f.get_id() == id_funcionario), None)
        projeto = next((p for p in projetos if p.get_codigo() == projeto_codigo), None)

        if funcionario and projeto:
            alocacao.set_funcionario(funcionario)
            alocacao.set_projeto(projeto)
            alocacao.set_data_inicio_alocacao(data_inicio_alocacao)
            print("Alocação atualizada com sucesso.")
        else:
            print("Funcionário ou projeto não encontrados.")
    else:
        print("Alocação não encontrada.")

def remover_funcionario():
    id = int(input("Digite o ID do funcionário que deseja remover: "))
    global funcionarios
    funcionarios = [f for f in funcionarios if f.get_id() != id]
    print("Funcionário removido com sucesso.")

def remover_projeto():
    codigo = int(input("Digite o código do projeto que deseja remover: "))
    global projetos
    projetos = [p for p in projetos if p.get_codigo() != codigo]
    print("Projeto removido com sucesso.")

def remover_alocacao():
    id_funcionario = int(input("Digite o ID do funcionário da alocação que deseja remover: "))
    projeto_codigo = int(input("Digite o código do projeto da alocação que deseja remover: "))
    global alocacoes
    alocacoes = [a for a in alocacoes if not (a.get_funcionario().get_id() == id_funcionario and a.get_projeto().get_codigo() == projeto_codigo)]
    print("Alocação removida com sucesso.")

def executar_menu_crud(tipo):
    while True:
        menu_crud(tipo)
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            if tipo == 'projeto':
                adicionar_projeto()
            elif tipo == 'funcionario':
                adicionar_funcionario()
            elif tipo == 'alocacao':
                adicionar_alocacao()
        elif escolha == '2':
            if tipo == 'projeto':
                listar_projetos()
            elif tipo == 'funcionario':
                listar_funcionarios()
            elif tipo == 'alocacao':
                listar_alocacoes()
        elif escolha == '3':
            if tipo == 'projeto':
                atualizar_projeto()
            elif tipo == 'funcionario':
                atualizar_funcionario()
            elif tipo == 'alocacao':
                atualizar_alocacao()
        elif escolha == '4':
            if tipo == 'projeto':
                remover_projeto()
            elif tipo == 'funcionario':
                remover_funcionario()
            elif tipo == 'alocacao':
                remover_alocacao()
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

def main():
    while True:
        menu_principal()
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            executar_menu_crud('projeto')
        elif escolha == '2':
            executar_menu_crud('funcionario')
        elif escolha == '3':
            executar_menu_crud('alocacao')
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
