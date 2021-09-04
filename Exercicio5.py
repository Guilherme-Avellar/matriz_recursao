def soma_vetor (vetor, tamanho):
    if tamanho == 0:
        return 0
    else:
        return vetor[tamanho - 1] + soma_vetor(vetor, tamanho - 1)




print(soma_vetor([1, 2, 3, 4, 5], 5))