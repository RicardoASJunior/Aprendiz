alunos = {
    "João": [8.5, 5.5, 7.0],
    "Maria": [9.5, 8.0, 9.0]
}

opcoes_menu = {
    1 : "1 - Cadastrar Aluno",
    2 : "2 - Alterar notas",
    3 : "3 - Ver nota",
    4 : "4 - Listar todas as notas",
    5 : "5 - Remover aluno",
    6 : "6 - Sair"
}

def cadastro_notas(nome_aluno):
    nota_primeira_prova = float(input("Informe a nota da primeira nota: " ))
    sc = validar_nota(nota_primeira_prova)
    if sc == 0: return

    nota_segunda_prova = float(input("Informe a nota da segunda nota: " ))
    sc = validar_nota(nota_segunda_prova)
    if sc == 0: return

    media_nota = (nota_primeira_prova + nota_segunda_prova)/2

    alunos[nome_aluno] = [nota_primeira_prova, nota_segunda_prova, media_nota]

    print("Cadastro realizado com sucesso!")

def cadastro_aluno():
    nome_aluno = input("Informe o nome do Aluno: ").strip().casefold()

    if nome_aluno == "":
        print("Aluno não informado!")
        return

    verificacao = verificar_registro(nome_aluno)
    if verificacao == True :
        print(f"Aluno {nome_aluno} já informado!")
        return

    cadastro_notas(nome_aluno)

def varificar_nota_aluno(nome_aluno):
    if nome_aluno.strip() == "":
        print("Aluno não informado!")
        print("\n")
        return
    
    verificacao = verificar_registro(nome_aluno)
    if verificacao == False : return

    notas = alunos[nome_aluno]
    separador()
    print(f"Aluno {nome_aluno}")
    for indice, nota in enumerate(notas):
        if indice == 0:
            print(f"Nota primeira prova:  {nota}")
        elif indice == 1:
            print(f"Nota segunda prova: {nota}")
        else:
            print(f"Média Final: {nota}")
            separador()

def verificar_notas_alunos():
    for nome_aluno in alunos:
        varificar_nota_aluno(nome_aluno)

def validar_nota(nota):
    if nota >= 0 and nota <= 10:
        return 1

    if nota < 0:
        print("Nota informada não pode ser menor que 0!")
        print("\n")
        return 0
    elif nota > 10:
        print("Nota não pode ser maior que 10!")
        print("\n")
        return 0
    else:
        print("Valor inválido!")
        print("\n")
        return 0

def remover_aluno():
    nome_aluno = input("Digite o nome para deletar: ").strip().casefold()
    print("\n")

    verificacao = verificar_registro(nome_aluno)
    if verificacao == False : return

    del alunos[nome_aluno]

    print(f"{nome_aluno} removido com sucesso!")
    print("\n")
    return

def verificar_registro(nome_aluno):
    if nome_aluno not in alunos:
        print(f"Nome {nome_aluno} não está registrado!")
        print("\n")
        return False
    return True

def separador():
    print("============================\n")

def menu():
    while True:
        for opcao in opcoes_menu.values():
            print(opcao)
        print("\n")

        escolha = input("Digite a opção desejada: ")

        if escolha == "1":
            separador()
            cadastro_aluno()
            separador()
        elif escolha == "2":
            separador()
            nome_aluno = input("Digite o nome do aluno que deseja alterar as notas: ")
            cadastro_notas(nome_aluno)
            separador()
        elif escolha == "3":
            separador()
            nome_aluno = input("Digite o nome do aluno que deseja acessar as notas: ")
            varificar_nota_aluno(nome_aluno)
            separador()
        elif escolha == "4":
            separador()
            verificar_notas_alunos()
            separador()
        elif escolha == "5":
            separador()
            remover_aluno()
            separador()
        elif escolha == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida!\n")

menu()