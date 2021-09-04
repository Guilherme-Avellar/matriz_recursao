# 4.Faça uma função que recebe, por parâmetro, uma matriz 6x6 e retorna o menor elemento da sua diagonal secundária.


def menor_num_diagonal_secundaria(matriz):
    menor = matriz[0][len(matriz) - 1]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i + j == len(matriz) - 1:
                if matriz[i][j] < menor:
                    menor = matriz[i][j]
    return menor


matriz1 = [[1, 2, 3, 4, 5, 6],
           [1, 2, 3, 4, 5, 6],
           [1, 2, 3, 4, 5, 6],
           [1, 2, 3, 4, 5, 6],
           [1, 2, 3, 4, 5, 6],
           [1, 2, 3, 4, 5, 6]
]

print(menor_num_diagonal_secundaria(matriz1))