#.n Renan Tiago dos Santos Silva
#.u 9793606

import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.patches import RegularPolygon

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

                        if (l%n!=j or o%m!=k) and (l%n,o%m) in lista:
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
    if n%2 != 0:
        n = n+1
    
    for i in range(t):
        for j in range(n):
            for k in range(m):
                
                vizinhos = 0
                for l in range(j-1, j+2):
                    for o in range(k-1, k+2):
                        if (l%n!=j or o%m!=k) and (l%n,o%m) in lista:
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

#celulas vivas são amarelas e as mortas são cinza
def desenhaQuad(n,m, lista, figura): 

    #define o tamanho do quadrado pelo circulo circunscrito   
    raio = 5
    apot = math.sqrt(2)*raio/2

    fig = plt.figure(figsize=(10, 10), dpi=100)
    ax = fig.add_subplot(111, aspect='equal', xlim = (0,2*apot*n), ylim = (0,2*apot*m))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    plt.title("Conway's Game of Life")

    for x in range(n):
        for y in range(m):
            patch = (apot + 2*apot*x, apot + 2*apot*y)
            if (x,y) in lista:
                quadrado = RegularPolygon(patch,4,raio,orientation = np.pi/4, facecolor = "yellow")
                ax.add_patch(quadrado)
            else:
                quadrado = RegularPolygon(patch,4,raio,orientation = np.pi/4, facecolor = "gray")
                ax.add_patch(quadrado)

    ax.autoscale_view()
    plt.savefig(figura, format= 'png')
    
#celulas vivas são brancas e as mortas são pretas
def desenhaHex(n,m,lista, figura):
    
    #define tamanho do hexagono pelo circulo circunscrito
    raio = 5
    apot = (raio* math.sqrt(3))/2

    fig = plt.figure(figsize=(10, 10), dpi=100)
    ax = fig.add_subplot(111, aspect='equal', xlim = (0,2*raio + 1.5*raio*(n-1)), ylim = (0,3*apot + 2*apot*(m-1)))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    plt.title("Conway's Game of Life")

    for x in range(n):
        for y in range(m):
            if x%2==0:
                patch = (raio +1.5*x*raio,2*apot + 2*apot*y)
            else:
                patch = (raio +1.5*x*raio,apot + 2*apot*y)

            if (x,y) in lista:

                hexagono = RegularPolygon(patch,6,raio,orientation = np.pi/6, facecolor = "yellow")
                ax.add_patch(hexagono)
            else:
                hexagono = RegularPolygon(patch,6,raio,orientation = np.pi/6, facecolor = "grey")
                ax.add_patch(hexagono)
    ax.autoscale_view()
    plt.savefig(figura, format= 'png')
    
def simulaQuadGenerica(n,m,lista, t,b,s):
    lista_tmp = []
    for i in range(t):
        for j in range(n):
            for k in range(m):
                
                vizinhos = 0
                for l in range(j-1, j+2):
                    for o in range(k-1, k+2):

                        if (l%n!=j or o%m!=k) and (l%n,o%m) in lista:
                            vizinhos = vizinhos+1

                if (j,k) in lista and vizinhos==s:
                    lista_tmp.append((j,k))
                elif vizinhos == b:
                    lista_tmp.append((j,k))
        lista = lista_tmp
        lista_tmp = []
    return lista

def simulaHexGenerica(n,m,lista,t,b,s):
    lista_tmp = []
    
    #caso onde numero de colunas é ímpar não permite unir as bordas, então somei uma borda
    #imaginária, com todas as células mortas
    if n%2 != 0:
        n = n+1
    
    for i in range(t):
        for j in range(n):
            for k in range(m):
                
                vizinhos = 0
                for l in range(j-1, j+2):
                    for o in range(k-1, k+2):
                        if (l%n!=j or o%m!=k) and (l%n,o%m) in lista:
                            if m%2==0 and not(l == j+1 and o!=k):
                                vizinhos = vizinhos+1
                            elif m%2!=0 and not(l == j-1 and o!=k):
                                vizinhos = vizinhos+1
                       
                if (j,k) in lista and vizinhos==s:
                    lista_tmp.append((j,k))
                elif not((j,k) in lista) and vizinhos == b:
                    lista_tmp.append((j,k))
        lista = lista_tmp
        lista_tmp = []
    return lista

def haRepeticoes(n,m,lista,t):
    lista_tmp = lista
    listas = [lista_tmp]
    repeticoes = False

    i = 0
    
    while i < t and not repeticoes:
        lista_tmp = simulaQuad(n,m,lista_tmp, 1)
        repeticoes = lista_tmp in listas
        listas.append(lista_tmp)
        i = i+1
    
    return repeticoes
