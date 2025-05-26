#Setando variáveis
"""
nome = "João"       # str
idade = 25          # int
altura = 1.80       # float
ativo = True        # bool
inativo = False        # bool
nameUser = ""

nameUser = input("Digite seu nome: ")
print(f"Olá, {id(nome)}!")
print(f"Olá, {nameUser}!")
print(f"idade, {idade}!")
print(f"altura, {altura}!")
print(f"ativo, {ativo}!")

a = "texto"
b = "texto"

print(id(a) == id(b))  # True — mesmo objeto

"""

# ================================================

#Trabalhando com IF / ELSE
"""

idade = 20

if idade >= 18:
    print(f"Maior idade {idade}")
elif idade > 0:
    print(f"Menor idade {idade}")
else: 
    print(f"Idade Inválida")

"""

# ================================================

# Trabalhando for em lista
"""

frutas = ["maçã", "banana", "uva", "maça verde", "Cajú", "Amendoim"]

for fruta in frutas:
    if fruta == "maçã":
        frutas.append("laranja")
    elif fruta == "laranja":
        print(f"Achou! {fruta}")

"""

# ================================================

# trabalhando com Dicionários
"""
usuarios = {
    "user1": {"nome": "Alice", "idade": 28},
    "user2": {"nome": "Bruno", "idade": 34},
    "user3": {"nome": "Clara", "idade": 22}
}

# user_id e dados foram variáveis que eu criei.. usuários.items() é o meu dicionário... user_id é o valor da primeira chave e dados é o outro dicionário dentro da minha chave
for user_id, dados in usuarios.items():
    print(f"ID: {user_id}")
    print(f"  Nome: {dados['nome']}")
    print(f"  Idade: {dados['idade']}")

for user_id, dados in usuarios.items():
    print(f"ID: {user_id}")
    for campo, valor in dados.items():
        print(f"  {campo.capitalize()}: {valor}")

"""

# ================================================

# esqueleto das funções

"""

def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Lucas"))

def somar(a, b=0):
    return print(a + b)

a=1
somar(a)

"""

# ================================================