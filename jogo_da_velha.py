# jogo da velha - Guilherme Carneiro Avellar (sozinho)

def fazer_jogada(linha, coluna, player, matriz_jogo, matriz_jogo_teste):
    if player == 1:
        matriz_jogo[linha][coluna] = "x"
        matriz_jogo_teste[linha][coluna] = 1
    else:
        matriz_jogo[linha][coluna] = "0"
        matriz_jogo_teste[linha][coluna] = 4

    return matriz_jogo

def arrumar_visual(matri_jogo):
    print("     0    1    2\n")
    print(f"0     {matri_jogo[0][0]} | {matri_jogo[0][1]} | {matri_jogo[0][2]}")
    print(f"1     {matri_jogo[1][0]} | {matri_jogo[1][1]} | {matri_jogo[1][2]}")
    print(f"2     {matri_jogo[2][0]} | {matri_jogo[2][1]} | {matri_jogo[2][2]}")
    return ""

def verificar_pontos(matriz_jogo, velha):
                                      #soma = 6 , 9 , 10 -> velha; soma = 3 -> player 1 ganha, 12 -> player 2 ganha
    contador1 = 0
    contador2 = 0
    contador3 = 0
    contador4 = 0
    soma = 0
    while contador2 != 3:                            #vertical colunas, vertical
        while contador3 != 3:                           # 0,0 + 1,0 + 2,0 | 0,1 + 1,1 + 2,1 | 0,2 + 1,2 + 2,2
            for i in range(len(matriz_jogo)):
                soma = soma + matriz_jogo[i][contador3]
            contador3 = contador3 + 1
            if soma == 3:
                print("Player 1 ganhou")
                contador3 = 3
                contador2 = 3
                contador1 = 1
            if soma == 12:
                print("Player 2 ganhou")
                contador3 = 3
                contador2 = 3
                contador1 = 1
            if soma == 9 or soma == 6  or soma == 10:
                velha = velha + 1
            if contador3 == 3:
                contador2 = 3
                #break
            soma = 0

        for i in range(len(matriz_jogo)):                #diagonal primaria
            soma = soma + matriz_jogo[i][i]
        if soma == 3:
            print("Player 1 ganhou")
            contador1 = 1
            contador2 = 3
        else:
            if soma == 12:
                print("Player 2 ganhou")
                contador1 = 1
                contador2 = 3
            else:
                if soma == 6 or soma == 9 or soma == 10:
                    velha = velha + 1
                    contador2 = 3

        soma = 0

        for i in range(len(matriz_jogo)):              #diagonal secundária
            for j in range(len(matriz_jogo)):
                if i + j == len(matriz_jogo) - 1:
                    soma = soma + matriz_jogo[i][j]
            if soma == 3:
                print("Player 1 ganhou")
                contador1 = 1
                contador2 = 3
            else:
                if soma == 12:
                    print("Player 2 ganhou")
                    contador1 = 1
                    contador2 = 3
                else:
                    if soma == 6 or soma == 9 or soma == 10:
                        velha = velha + 1
                        contador2 = 3
        soma = 0

        while contador4 != 3:                           # 0,0 + 0,1 + 0,2 | 1,0 + 1,1 + 1,2 | 2,0 + 2,1 + 2,2
            for j in range(len(matriz_jogo)):           # linhas
                soma = soma + matriz_jogo[contador4][j]
            contador4 = contador4 + 1
            if soma == 3:
                print("Player 1 ganhou")
                contador4 = 3
                contador2 = 3
                contador1 = 1
            if soma == 12:
                print("Player 2 ganhou")
                contador4 = 3
                contador2 = 3
                contador1 = 1
            if soma == 9 or soma == 6 or soma == 10:
                velha = velha + 1
            if contador4 == 3:
                contador2 = 3
                #break
            soma = 0

        if soma == 0:
            contador2 = 3

    if velha == 8:                             # 3 colunas + 3 linha + 2 diagonais
        print("Velha")
        contador1 = 1

    return contador1


matriz_jogo = [[" ", " ", " "],
               [" ", " ", " "],
               [" ", " ", " "]
]
matriz_jogo_teste = [[5, 5, 5],
                     [5, 5, 5],
                     [5, 5, 5]
]
velha = 0

print("\n                            Jogo Da Velha\n")
print("obs: escolha da linha 0 a 2, da coluna 0 a 2. \n")
print(arrumar_visual(matriz_jogo))


contador = 0
contador1 = 0
while contador1 != 1:
    while contador != 2:
        print("                  Player 1 (x)")
        linha_player1 = int(input("Digite a linha: "))
        coluna_player1 = int(input("Digite a coluna: "))
        if linha_player1 > 2 or linha_player1 < 0 or coluna_player1 > 2 or coluna_player1 < 0:
            print("Valor inválido")
        else:
            if matriz_jogo[linha_player1][coluna_player1] == "x" or matriz_jogo[linha_player1][coluna_player1] == "0":
                print("Essa jogada já foi feita")
            else:
                matriz_jogo = fazer_jogada(linha_player1, coluna_player1, 1, matriz_jogo, matriz_jogo_teste)
                print("\n")
                print(arrumar_visual(matriz_jogo))
                print("\n")
                contador1 = verificar_pontos(matriz_jogo_teste, velha)
                contador = 2

    if contador1 == 1:
        contador = 3

    while contador != 3:
        print("\n                  Player 2 (0)")
        linha_player2 = int(input("Digite a linha: "))
        coluna_player2 = int(input("Digite a coluna: "))
        if linha_player2 > 2 or linha_player2 < 0 or coluna_player2 > 2 or coluna_player2 < 0:
            print("Valor inválido")
        else:
            if matriz_jogo[linha_player2][coluna_player2] == "x" or matriz_jogo[linha_player2][coluna_player2] == "0":
                print("Essa jogada já foi feita")
            else:
                matriz_jogo = fazer_jogada(linha_player2, coluna_player2, 2, matriz_jogo, matriz_jogo_teste)
                print("\n")
                print(arrumar_visual(matriz_jogo))
                print("\n")
                contador1 = verificar_pontos(matriz_jogo_teste, velha)
                contador = 3