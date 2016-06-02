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

def main():
    grade, pares = leEntrada("arquivo.txt")
    
main()