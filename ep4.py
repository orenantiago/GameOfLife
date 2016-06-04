import matplotlib.pyplot as plt
import numpy as np

def leEntrada(nome):
    f = open(nome, "r")
    grade = 0;
    primeira_linha = True;
    pares = []

    for linha in f:
        linha = linha.replace("\n","")
        if primeira_linha == True:
            if linha == 'H':
                grade = 1
            primeira_linha = False
        else:
            numeros = linha.split(',', 1)
            pares = pares + [(int(numeros[0]),int(numeros[1]))]
    return grade, pares
    f.close()

def simulaQuad(n,m,lista, t):
    lista_tmp = []
    for i in range(t):
        for j in range(n):
            for k in range(m):
                
                vizinhos = 0
                for l in range(j-1, j+2):
                    for o in range(k-1, k+2):

                        if (l!=j or o!=k) and (l%n,o%m) in lista:
                            vizinhos = vizinhos+1

                if (j,k) in lista and 2<=vizinhos<=3:
                    lista_tmp.append((j,k))
                elif vizinhos == 3:
                    lista_tmp.append((j,k))
        lista = lista_tmp
        lista_tmp = []
    return lista

def simulaHex(n,m,lista,t):
    lista_tmp = []
    
    #caso onde numero de colunas é ímpar não permite unir as bordas, então somei uma borda
    #imaginária, com todas as células mortas
    if m%2 != 0:
        m = m+1
    
    for i in range(t):
        for j in range(n):
            for k in range(m):
                
                vizinhos = 0
                for l in range(j-1, j+2):
                    for o in range(k-1, k+2):
                        if (l!=j or o!=k) and (l%n,o%m) in lista:
                            if m%2==0 and not(l == j+1 and o!=k):
                                vizinhos = vizinhos+1
                            elif m%2!=0 and not(l == j-1 and o!=k):
                                vizinhos = vizinhos+1
                       
                if (j,k) in lista and vizinhos==2:
                    lista_tmp.append((j,k))
                elif not((j,k) in lista) and (vizinhos == 3 or vizinhos == 5):
                    lista_tmp.append((j,k))
        lista = lista_tmp
        lista_tmp = []
    return lista

def desenhaQuad(n,m, lista,figura):
    coordenadas = np.zeros((n,m))
    for i in range(len(lista)):
        x,y = lista[i][0], lista[i][1]
        coordenadas[x, y] = 1
    plt.matshow(coordenadas, cmap =plt.cm.gray)
    plt.savefig(figura, format= 'png')

def main():
    grade, pares = leEntrada("20x20_glider.txt")
    lista = simulaQuad(20,20,pares,2)
    print(lista)
    desenhaQuad(20,20,lista, "figura")
    
main()