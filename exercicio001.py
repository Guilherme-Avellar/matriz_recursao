# 1. Faça uma função que recebe, por parâmetro, uma matriz 5x5 e retorna a soma dos seus elementos.

def somar_matriz(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma = soma + matriz[i][j]
    return soma

matriz1 = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 9, 5]]
print(somar_matriz(matriz1))