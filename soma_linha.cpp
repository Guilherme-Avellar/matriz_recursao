#include <bits/stdc++.h>

using namespace std;

#define N 3

int somar_linha(int matriz[N][N], int tam);

int main(){

    int matriz[N][N], i, j, soma[N];

    for(i = 0; i < N; i++){
        for(j = 0; j < N; j++){
            cin >> matriz[i][j];
        }
    }

    for(i = 0; i < N; i++){
        soma[i] = 0;
        for(j = 0; j < N; j++){
            soma[i] += matriz[i][j];
        }
    }

    for(i = 0; i < N; i++){
        printf("Linha %d: %d\n", i, soma[i]);
    }

    return 0;
}
