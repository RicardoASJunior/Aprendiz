frase = "Python é demais!"

tupla_vogais = ("a","e","i","o","u","á","é","í","ó","ú","à")

def buscar_vogais(frase):
    contador=0

    for letra in frase:
        if letra.casefold() in tupla_vogais:
            contador+=1
    
    return contador

quantidade = buscar_vogais(frase)
print(f"Foram encontrados {quantidade} vogais!")