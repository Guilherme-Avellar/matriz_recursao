# 2.Faça uma função que recebe, por parâmetro, uma matriz 6x6 e retorna a soma dos elementos da sua diagonal principal
# e da sua diagonal secundária.

# def diagonal_principal(matriz):
#     soma = 0
#     for i in range(len(matriz)):
#         for j in range(len(matriz[0])):
#             if i == j:
#                 soma = soma + matriz[i][j]

def diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma = soma + matriz[i][i]    # matriz[i][i] pq precisa somar os elementos em que i e j são iguais... então para simplificar coloca o i nos dois
    return soma

def diagonal_secundaria(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i + j == len(matriz) - 1:
                soma = soma + matriz[i][j]

    return soma

matriz1 = [[1, 2, 3, 4, 5, 6],
           [1, 2, 3, 4, 5, 6],
           [1, 2, 3, 4, 5, 6],
           [1, 2, 3, 4, 5, 6],
           [1, 2, 3, 9, 5, 6],
           [1, 2, 3, 9, 5, 6]
]
print(len(matriz1))
print(diagonal_principal(matriz1))
print(diagonal_secundaria(matriz1))