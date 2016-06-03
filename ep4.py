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
                #print(j,k, " vizinhos:")
                for l in range(j-1, j+2):
                    for o in range(k-1, k+2):

                        if (l!=j or o!=k) and (l%n,o%m) in lista:
                            #print(l%n,o%m)
                            vizinhos = vizinhos+1

                if (j,k) in lista and 2<=vizinhos<=3:
                    lista_tmp.append((j,k))
                elif vizinhos == 3:
                    lista_tmp.append((j,k))
        lista = lista_tmp
        lista_tmp = []
    return lista




def main():
    grade, pares = leEntrada("arquivo.txt")
    lista = simulaQuad(4,4,pares,3)
    print(lista)
    
main()