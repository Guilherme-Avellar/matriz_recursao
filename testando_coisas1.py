from random import *

def criar_matriz(dimensao):
    matriz = []
    for i in range(dimensao):
        linha = []
        for j in range(dimensao):
            linha.append(" _ ")
        matriz.append(linha)
    return matriz

def exibir_matriz(matriz):
    print()
    print(" " * 19, end="")
    for i in range(dimensao):
        print(f"{i:3d} ", end="")
    print()
    for i in range(dimensao):
        print(" " * 14, end= "")
        print(f"{i:3d}   ", end="")
        for j in range(dimensao):
            print(f"{matriz[i][j]} ", end="")
        print("")
    print()

def sortear_minas(matriz):
    dimensao = len(matriz)
    cont_minas = 0
    while cont_minas < dimensao:
        linha = randint(0, dimensao - 1)
        coluna = randint(0, dimensao - 1)
        if matriz[linha][coluna] != " * ":
            matriz[linha][coluna] = " * "
            cont_minas = cont_minas + 1
    return matriz

def calcular_vizinhanca(matriz):
    dimensao = len(matriz)
    for i in range(dimensao):
        for j in range(dimensao):

            if matriz[i][j] != " * ":

                linha_inicial = i - 1
                if linha_inicial < 0:
                    linha_inicial = 0
                linha_final = i + 1
                if linha_final > dimensao - 1:
                    linha_final = dimensao - 1
                coluna_inicial = j - 1
                if coluna_inicial < 0:
                    coluna_inicial = 0
                coluna_final = j + 1
                if coluna_final > dimensao - 1:
                    coluna_final = dimensao - 1

                valor = 0
                for l in range(linha_inicial, linha_final + 1):
                    for c in range(coluna_inicial, coluna_final + 1):
                        if matriz[l][c] == " * ":
                            valor = valor + 1
                if valor != 0:
                    matriz[i][j] = (f" {valor} ")

    return matriz

def abrir_matriz(matriz, matriz_implicita, i, j):
    dimensao = len(matriz)

    if matriz_implicita[i][j] == " _ ":
        matriz_implicita[i][j] = "   "
        matriz[i][j] = "   "

        linha_inicial = i - 1
        if linha_inicial < 0:
            linha_inicial = 0
        linha_final = i + 1
        if linha_final > dimensao - 1:
            linha_final = dimensao - 1
        coluna_inicial = j - 1
        if coluna_inicial < 0:
            coluna_inicial = 0
        coluna_final = j + 1
        if coluna_final > dimensao - 1:
            coluna_final = dimensao - 1

        for l in range(linha_inicial, linha_final + 1):
            for c in range(coluna_inicial, coluna_final + 1):
                abrir_matriz(matriz, matriz_implicita, l, c)

def mostrar_numeros(matriz, matriz_implicita, linha, coluna):
    dimensao = len(matriz)

    linha_inicial = linha - 1
    if linha_inicial < 0:
        linha_inicial = 0
    linha_final = linha + 1
    if linha_final > dimensao - 1:
        linha_final = dimensao - 1
    coluna_inicial = coluna - 1
    if coluna_inicial < 0:
        coluna_inicial = 0
    coluna_final = coluna + 1
    if coluna_final > dimensao - 1:
        coluna_final = dimensao - 1


    if matriz_implicita[i][j] == "   ":
        for l in range(linha_inicial, linha_final + 1):
            for c in range(coluna_inicial, coluna_final + 1):
                if matriz_implicita[l][c] != " * " or matriz_implicita[l][c] != "   ":
                    matriz[l][c] = matriz_implicita[l][c]

def condicao_vitoria():
    contador = 0
    for i in range(dimensao):
        for j in range(dimensao):
            if matriz[i][j] == " M " and matriz_implicita[i][j] == " * ":
                contador = contador + 1
            if matriz[i][j] == " _ ":
                contador = contador + 1

    return contador

dimensao = 4

matriz = criar_matriz(dimensao)
matriz_implicita = criar_matriz(dimensao)

matriz_implicita = sortear_minas(matriz_implicita)
matriz_implicita = calcular_vizinhanca(matriz_implicita)

exibir_matriz(matriz)
exibir_matriz(matriz_implicita)

num_jogadas = 0

fim_jogo = False

print(f"Existem {dimensao} minas no jogo\n")

while not fim_jogo:
    condicao_ok = False

    linha = int(input("Digite a linha: "))
    coluna = int(input("Digite a coluna: "))

    if linha > dimensao or linha < 0 or coluna > dimensao or coluna < 0:
        print("Jogada fora do tabuleiro.\n")
        condicao_ok = True
    else:
        if matriz[linha][coluna] != " _ ":
            print("Jogada já feita.\n")
            condicao_ok = True

        else:
            for i in range(dimensao):
                for j in range(dimensao):
                    if matriz_implicita[linha][coluna] == " * ":
                        if matriz_implicita[i][j] == " * ":
                            matriz[i][j] = " * "

            if matriz_implicita[linha][coluna] == " * ":
                print("\n\nFim de jogo.")
                fim_jogo = True
                condicao_ok = True

            else:
                if matriz_implicita[linha][coluna] == " _ ":
                    abrir_matriz(matriz, matriz_implicita, linha, coluna)
                    for i in range(dimensao):
                        for j in range(dimensao):
                            mostrar_numeros(matriz, matriz_implicita, i, j)

                else:
                    matriz[linha][coluna] = matriz_implicita[linha][coluna]


            if dimensao == condicao_vitoria():
                print("\n\nVitória.")
                fim_jogo = True
                condicao_ok = True

            exibir_matriz(matriz)

    while not condicao_ok:
        condicao = input("Deseja marcar ou desmarcar uma mina? (s/n): ").upper()
        print()
        if condicao == "N":
            condicao_ok = True
        else:
            if condicao == "S":
                linha_marca = int(input("Linha da marca: "))
                coluna_marca = int(input("Coluna da marca: "))
                if matriz[linha_marca][coluna_marca] == " _ ":
                    matriz[linha_marca][coluna_marca] = " M "
                    condicao_ok = True
                else:
                    if matriz[linha_marca][coluna_marca] == " M ":
                        matriz[linha_marca][coluna_marca] = " _ "
                        condicao_ok = True
                    else:
                        print("Este local não pode ser marcado")

                exibir_matriz(matriz)