# Função para cadastrar um colaborador
def cadastrar_colaborador(id):
    print("****************************************************************************************")
    print("-------------------------------MENU CADASTRAR COLABORADOR-------------------------------")
    print(f"ID do colaborador {id}")
    nome = input("Por favor entre com o nome: ")
    setor = input("Por favor entre com setor: ")
    pagamento = float(input("Por favor entre com o pagamento (R$): "))
    
    colaborador = {
        "ID": id,
        "Nome": nome,
        "Setor": setor,
        "Pagamento": pagamento
    }
    
    lista_colaboradores.append(colaborador)

# Função para consultar os colaboradores
def consultar_colaborador():
    print("****************************************************************************************")
    print("-------------------------------MENU CONSULTAR COLABORADOR-------------------------------")
    opcao = input("Escolha a opção desejada:\n1. Consultar Todos os Colaboradoes\n2. Consultar Colaborador por ID\n3. Consultar Colaborador(es) por Setor\n4. Retornar\n")
    
    if opcao == '1':
        print("--------------------------------------------")
        for colaborador in lista_colaboradores:
            print(f"id : {colaborador['ID']}\nnome : {colaborador['Nome']}\nsetor : {colaborador['Setor']}\npagamento : {colaborador['Pagamento']}")
            print("--------------------------------------------")
    elif opcao == '2':
        id_consulta = int(input("Digite o ID do colaborador: "))
        print("--------------------------------------------")
        for colaborador in lista_colaboradores:
            if colaborador["ID"] == id_consulta:
                print(f"id : {colaborador['ID']}\nnome : {colaborador['Nome']}\nsetor : {colaborador['Setor']}\npagamento : {colaborador['Pagamento']}")
                print("--------------------------------------------")
                break
    elif opcao == '3':
        setor_consulta = input("Digite o setor do(s) colaborador(es): ")
        print("--------------------------------------------")
        for colaborador in lista_colaboradores:
            if colaborador["Setor"] == setor_consulta:
                print(f"id : {colaborador['ID']}\nnome : {colaborador['Nome']}\nsetor : {colaborador['Setor']}\npagamento : {colaborador['Pagamento']}")
                print("--------------------------------------------")
    elif opcao == '4':
        return
    else:
        print("Opção inválida.")

# Função para remover um colaborador
def remover_colaborador():
    print("****************************************************************************************")
    print("--------------------------------MENU REMOVER COLABORADOR--------------------------------")
    id_remocao = int(input("Digite o ID do colaborador a ser removido: "))
    for colaborador in lista_colaboradores:
        if colaborador["ID"] == id_remocao:
            lista_colaboradores.remove(colaborador)
            print("Colaborador removido com sucesso.")
            break

print("Bem-vindo ao Controle de Colaboradores")

# Declarando o vetor que armazena os colaboradores
lista_colaboradores = []
id_global = 0

# Funcção do menu principal
while True:
    print("****************************************************************************************")
    print("-------------------------------------MENU PRINCIPAL-------------------------------------")
    opcao_menu = input("Escolha uma opção:\n1. Cadastrar Colaborador\n2. Consultar Colaborador\n3. Remover Colaborador\n4. Retornar\n")
    
    if opcao_menu == '1':
        id_global += 1
        cadastrar_colaborador(id_global)
    elif opcao_menu == '2':
        consultar_colaborador()
    elif opcao_menu == '3':
        remover_colaborador()
    elif opcao_menu == '4':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida.")