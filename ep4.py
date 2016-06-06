import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.collections import RegularPolyCollection

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

#celular vivas são brancas e as mortas são pretas
def desenhaQuad(n,m, lista, figura):
    coordenadas = np.zeros((n,m))
    if lista != []:
        for i in range(len(lista)):
            x,y = lista[i][0], lista[i][1]
            coordenadas[x, y] = 1
    plt.matshow(coordenadas, cmap =plt.cm.gray)
    plt.savefig(figura, format= 'png')
    
#celulas vivas são brancas e as mortas são pretas
def desenhaHex(n,m,lista, figura):
    offset = []
    facecolors = []
    
    #define tamanho do hexagono pelo circulo circunscrito
    raio = 30
    area = raio*np.pi**2
    apot = (2*raio* math.sqrt(3))/9

    for x in range(n):
        for y in range(m):
            if (x,y) in lista:
                facecolors+= ['white',]
            else:
                facecolors+=['black',]
            if x%2 == 0:
                offset += [x*1.5*raio,(y*2*apot)+apot]
            else:
                offset += [x*1.5*raio,(y*2*apot)]

    x_maximo = (n-1)*1.5*raio+ raio
    x_minimo = -raio
    y_maximo = (m-1)*2*apot + raio
    y_minimo = -raio

    fig = plt.figure(figsize=(10, 10), dpi=100)
    ax = fig.add_subplot(111)
    #ax.axis([x_minimo,x_maximo , y_minimo, y_maximo])
    
    #gera hexagonos
    collection = RegularPolyCollection(
        numsides=6,
        rotation=np.pi/6, 
        sizes=(area,),
        facecolors = facecolors,
        edgecolors = ('blue',),
        linewidths = (1,),
        offsets = offset,
        transOffset = ax.transData,
        )
    ax.add_collection(collection, autolim=True)
    ax.autoscale_view()
    #plt.savefig(figura, format= 'png')
    plt.show()
    
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
    if m%2 != 0:
        m = m+1
    
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

def main():
    grade, pares = leEntrada("arquivo.txt")
    #pares = [(0,0)]
    lista = simulaHexGenerica(4,4,pares,5,0,0)
    desenhaHex(4,4, lista, "figura")
    print(lista)
main()
