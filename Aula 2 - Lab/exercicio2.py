# Exercício 2 - Melhorando Código Ineficiente

def calcular_media(notas):
    soma = 0
    for nota in notas:
        soma += nota
    return soma / len(notas)

notas = [7, 8, 9, 10]
print(calcular_media(notas))  # Esperado: 8.5




