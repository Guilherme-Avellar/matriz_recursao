# teste
def fazer_matriz(dimensao):
    matriz = []
    for i in range(dimensao):
        linha = []
        for j in range(dimensao):
            linha.append(f" _ ")
        matriz.append(linha)
    return matriz

def exibir_jogo(matriz):
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

def pontucao_necessaria():
    soma = 0
    if num_barcos > len(tamanho_barco):
        variar_tamanho = 0
        for i in range(num_barcos):
            tamanho_barco.append(1 + i + variar_tamanho)
            variar_tamanho = variar_tamanho + 1
    for i in range(num_barcos):
        soma = soma + tamanho_barco[i]

    return soma

def colocar_navios(matriz, jogador, linha, coluna, linha2, coluna2):
    if coluna == coluna2:
        for i in range(linha, linha2 + 1):
            if (matriz[i][coluna] == " @ " and jogador == " * ") or matriz[i][coluna] == " * " and jogador == " @ ":
                matriz[i][coluna] = " X "
            else:
                matriz[i][coluna] = jogador
    else:
        if linha == linha2:
            for j in range(coluna, coluna2 + 1):
                if (matriz[linha][j] == " @ " and jogador == " * ") or matriz[linha][j] == " * " and jogador == " @ ":
                    matriz[linha][j] = " X "
                else:
                    matriz[linha][j] = jogador


    return matriz

def arrumar_exibicao_jogo(tiro_linha, tiro_coluna):
    if matriz_implicita[tiro_linha][tiro_coluna] == " _ ":
        matriz[tiro_linha][tiro_coluna] = " ~ "
    else:
        matriz[tiro_linha][tiro_coluna] = matriz_implicita[tiro_linha][tiro_coluna]

    return exibir_jogo(matriz)



dimensao = 6
ganhou = False


matriz = fazer_matriz(dimensao)
matriz_implicita = fazer_matriz(dimensao)

num_barcos = dimensao // 3
tamanho_barco = []  # vários tamanhos de barcos

pontucao_necessaria()
pontos_necessarios = pontucao_necessaria()



jogador = ["   ", " * ", " @ "]

tiros = []

exibir_jogo(matriz)

for j in range(1, len(jogador)):
    print(f"jogador: {j}")
    for i in range(num_barcos, 0, -1):
        jogada = False
        while not jogada:
            if tamanho_barco[i - 1] == 1:
                print(f"Você tem {i} barco para esconder. Coloque sua linha e coluna")
                linha = int(input(("Digite a linha: ")))
                coluna = int(input("Digite a colua: "))
                print()
                linha2 = linha
                coluna2 = coluna
            else:
                print(f"Você tem {i} barcos para esconder. Escolha um intervalo de {tamanho_barco[i - 1]} casas que o navio vai ocupar")
                linha = int(input("1º Linha: "))
                coluna = int(input("1º Coluna: "))
                print("Até")
                linha2 = int(input("Última Linha: "))
                coluna2 = int(input("Última Coluna: "))
                print()
            if matriz_implicita[linha][coluna] == jogador[j] or matriz_implicita[linha2][coluna2] == jogador[j]:
                print("Jogada já feita. Não é permitido sobrepor seus navios")
            else:
                if linha > dimensao - 1 or coluna > dimensao - 1 or linha2 > dimensao - 1 or coluna2 > dimensao - 1:
                    print("Passou o número de casas")
                else:
                    if linha - linha2 == tamanho_barco[i - 1] - 1 or coluna - coluna2 == tamanho_barco[i - 1] - 1:
                        if coluna != coluna2 and linha != linha2:
                            print("Não é desta modalidade de jogo por o navio na diagonal")
                        else:
                            if linha2 < linha or coluna2 < coluna:
                                colocar_navios(matriz_implicita, jogador[j], linha2, coluna2, linha, coluna)
                            else:
                                colocar_navios(matriz_implicita, jogador[j], linha, coluna, linha2, coluna2)
                            jogada = True
                    else:
                        if linha2 - linha == tamanho_barco[i - 1] - 1 or coluna2 - coluna == tamanho_barco[i - 1] - 1:
                            if coluna != coluna2 and linha != linha2:
                                print("Não é desta modalidade de jogo por o navio na diagonal")
                            else:
                                if linha2 < linha or coluna2 < coluna:
                                    colocar_navios(matriz_implicita, jogador[j], linha2, coluna2, linha, coluna)
                                else:
                                    colocar_navios(matriz_implicita, jogador[j], linha, coluna, linha2, coluna2)
                                jogada = True
                        else:
                            print("Tamanho de ocupação do barco inválido com o que se pede.")


print("\n jogador 1 = * \n"
        " jogador 2 = @\n"
        " barcos de jogadores diferentes no mermo local = X\n")

tiros_vetor = []
tiros_matriz = []

pontos1 = 0
pontos2 = 0

jogada = False

contador = 1

while pontos1 < pontos_necessarios or pontos2 < pontos_necessarios:
    while not jogada:
        print(f"Vez do jogador {contador} atirar")
        tiro_linha = int(input("Digite a linha do tiro ao navio: "))
        tiro_coluna = int(input("Digite a coluna do tiro ao navio: "))
        if tiro_linha > dimensao - 1 or tiro_coluna > dimensao - 1:
            print("Tiro fora do tabuleiro.")
        else:
            if matriz[tiro_linha][tiro_coluna] == " @ " or matriz[tiro_linha][tiro_coluna] == " * " or matriz[tiro_linha][tiro_coluna] == " ~ ":
                print("jogada já feita")
            else:
                arrumar_exibicao_jogo(tiro_linha, tiro_coluna)

                if matriz_implicita[tiro_linha][tiro_coluna] == " @ ":
                    pontos1 = pontos1 + 1
                else:
                    if matriz_implicita[tiro_linha][tiro_coluna] == " * ":
                        pontos2 = pontos2 + 1
                    else:
                        if matriz_implicita[tiro_linha][tiro_coluna] == " X ":
                            pontos1 = pontos1 + 1
                            pontos2 = pontos2 + 1

        if pontos1 == pontos_necessarios and pontos2 == pontos_necessarios:
            print("Não acho que quem ganhar ou quem perder, nem quem ganhar nem perder, vai ganhar ou perder. "
                  "Vai todo mundo perder. (empate)")
            jogada = True
        else:
            if pontos1 == pontos_necessarios:
                print("Jogador 1 venceu.")
                jogada = True
            else:
                if pontos2 == pontos_necessarios:
                    print("Jogador 2 venceu.")
                    jogada = True

        if contador == 1:
            contador = 2
        else:
            contador = 1