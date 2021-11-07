#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Linha do Tempo Sagrada
# Nome: Osca Ciceri
# RA: 164786
#####################################################


def busqueda(i,j):
    aux = False
    fila = i
    colu = j 
    while(aux == False):
        # print(fila,colu)
        if(matriz[colu-1][fila]=="+"):
            matriz[colu][fila] = '#'
            colu-=1
            if(colu==0):
                aux = True
        elif(matriz[colu+1][fila]=="+"): 
            matriz[colu][fila] = '#'  
            colu+=1
            if(colu==10):
                aux = True
        elif(matriz[colu][fila+1]=="+"): 
            matriz[colu][fila] = '#'
            fila+=1
            if(fila==49):
                aux = True
        elif(matriz[colu][fila-1]=="+"):   
            matriz[colu][fila] = '#'
            fila-=1
            if(fila==0):
                aux = True
        else:
            aux = True

    valor = (fila,colu)
 
    return valor

def imprimir(ix,rta):
    if(rta[1]==0 or rta[1]==10 or rta[0]==49 or rta[0]==0):
        tipo = "Evento Nexus"
    else:
        tipo = "Instavel"
    ixx = str(ix)+":"
    print("Bifurcacao",ixx,tipo)
     
# Leitura da matriz

matriz = []
for i in range(11):
    matriz.append(list(input()))

# print(matriz)

# print('\n\n',matriz[5])

for i in range(len(matriz[5])):
    if(matriz[4][i] == '+'):
        rta = busqueda(i, 4)
        imprimir(i,rta)
    elif(matriz[6][i] == '+'):
        rta = busqueda(i, 6)
        imprimir(i,rta)



