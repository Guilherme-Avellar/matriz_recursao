# 3.Faça uma função que recebe, por parâmetro, uma matriz 7x6 e retorna a soma dos elementos da linha 5 e da coluna 3.

def somar_coluna(matriz, coluna):
    soma = 0
    for i in range(len(matriz)):
        soma = soma + matriz[i][coluna]
    return soma

def somar_linha(matriz, linha):
    soma = 0
    for j in range(len(matriz[0])):
        soma = soma + matriz[linha][j]
    return soma

matriz1 = [[1, 2, 3, 4, 5, 6],
           [1, 2, 3, 4, 5, 6],
           [1, 2, 3, 4, 5, 6],
           [1, 2, 3, 4, 5, 6],
           [1, 2, 3, 4, 5, 6],
           [1, 2, 3, 4, 5, 6],
           [1, 2, 3, 4, 5, 6]
]

linha = int(input("Digite qual a linha a somar: "))
coluna = int(input(f"Digite qual a coluna a somar com a linha {linha}: "))

print(f"Soma da coluna {coluna} com a linha {linha}: {somar_coluna(matriz1, coluna) + somar_linha(matriz1, linha)}")
