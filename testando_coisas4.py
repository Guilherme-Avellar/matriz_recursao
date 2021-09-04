def pontucao_necessaria():
    soma = 0
    if num_barcos > len(tamanho_barco):
        for i in range(num_barcos - len(tamanho_barco)):
            tamanho_barco.append(1 + i)
    for i in range(num_barcos):
        soma = soma + tamanho_barco[i]

    return soma

dimensao = 11
num_barcos = 11 // 3
tamanho_barco = []

pontos_necessarios = pontucao_necessaria()

print(pontucao_necessaria())
print(pontos_necessarios)
print(tamanho_barco)

for i in range(4):
    print(i)