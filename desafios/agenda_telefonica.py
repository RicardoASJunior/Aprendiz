agenda_telefonica = {
    "Ana" : "9999-0001",
    "Carlos" : "9999-0002"
} 

opcoes_menu = {
    1 : "1 - Adicionar Contato",
    2 : "2 - Alterar Contato",
    3 : "3 - Deletar Contato",
    4 : "4 - Verificar número",
    5 : "5 - Listar Registros",
    6 : "6 - Sair"
}

def adicionar_contato():
    nome_agenda = input("Digite o nome para adicionar: ").strip().casefold()

    if nome_agenda.strip().casefold() in agenda_telefonica:
        sim_nao = input(f"Nome {nome_agenda} já está cadastrado, deseja alterar (s/n)? ")
        
        if sim_nao.casefold() == "s":
            alterar_contato(nome_agenda)
            return
        else: 
            return
    numero_agenda = input("Digite o número: ")
    agenda_telefonica[nome_agenda] = numero_agenda

    print("Registro adicionado com sucesso!")
    print("\n")
    return

def alterar_contato(nome):
    verificacao = verificar_registro(nome)
    if verificacao == False : return

    numero_agenda = input("Digite o novo número: ")

    agenda_telefonica[nome] = numero_agenda

    print(f"Número {numero_agenda} alterado com sucesso")

def listar_registros(agenda_telefonica):
    for nome, valor in agenda_telefonica.items():
        print(f"{nome} : telefone: {valor}")
    return

def deletar_contato():
    nome_agenda = input("Digite o nome para deletar: ").strip().casefold()
    print("\n")

    verificacao = verificar_registro(nome_agenda)
    if verificacao == False : return

    del agenda_telefonica[nome_agenda]

    print(f"{nome_agenda} removido com sucesso!")
    print("\n")
    return

def verificar_numero(nome):
    verificacao = verificar_registro(nome)
    if verificacao == False : return

    print(f"{nome}, telefone : {agenda_telefonica[nome]}")

def verificar_registro(nome):
    if nome not in agenda_telefonica:
        print(f"Nome {nome} não está registrado!")
        print("\n")
        return False
    return True

# Forma que eu fiz, mas não é performático!
# def menu(opcoes_menu):
#     for opcoes in opcoes_menu:
#         print(opcoes_menu[opcoes])
# 
#     print("\n")
#     opcao = input("Digite a opção desejada: ")
# 
#     if opcao == "1":
#         adicionar_contato()
#     elif opcao == "2":
#         nome = input("Digite o nome para alterar: ")
#         alterar_contato(nome)
#     elif opcao == "3":
#         deletar_contato()
#     elif opcao == "4":
#         nome = input("Digite o nome que deseja acessar: ")
#         verificar_numero(nome)
#     elif opcao == "5":
#         listar_registros(agenda_telefonica)
#     else:
#         return
#     
#     menu(opcoes_menu)

def menu(opcoes_menu):
    while True:
        for opcao in opcoes_menu.values():
            print(opcao)
        print("\n")

        escolha = input("Digite a opção desejada: ")

        if escolha == "1":
            adicionar_contato()
        elif escolha == "2":
            nome = input("Digite o nome para alterar: ")
            alterar_contato(nome)
        elif escolha == "3":
            deletar_contato()
        elif escolha == "4":
            nome = input("Digite o nome que deseja acessar: ")
            verificar_numero(nome)
        elif escolha == "5":
            listar_registros(agenda_telefonica)
        elif escolha == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida!\n")


menu(opcoes_menu)