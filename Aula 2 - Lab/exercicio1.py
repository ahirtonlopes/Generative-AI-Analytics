# Exercício 1 - Gerando código a partir de comentários

# Escreva uma função que receba uma lista de números e retorne o maior número da lista

def maior(lista):
    return max(lista)

# Escreva uma função que receba uma lista de números e retorne o menor número da lista

def menor(lista):
    return min(lista)

# Escreva uma função que receba uma lista de números e retorne a média dos números

def media(lista):
    return sum(lista) / len(lista)

# Escreva uma função que receba uma lista de números e retorne a soma dos números

def soma(lista):
    return sum(lista)

# Escreva uma função que receba uma lista de números e retorne a quantidade de números na lista

def quantidade(lista):
    return len(lista)

# Escreva uma função que receba uma lista de números e retorne apenas os números pares

def pares(lista):
    return [x for x in lista if x % 2 == 0]
