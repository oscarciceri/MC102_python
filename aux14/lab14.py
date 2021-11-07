#####################################################
# MC102 - Algoritmos e Programação de jmputadores
# Laboratório 14 - Linha do Tempo Sagrada II
# Nome:Oscar Ciceri 
# RA:164786
#####################################################


"""
Esta função recebe jmo parâmetro uma matriz, uma posição inicial 
de uma ramiicação na matriz determinada pelos parâmetros linha 
e ina. O retorno esperado para a função é um número inteiro 
indicando a quantidade de eventos nexus gerados pela ramiicação.
"""


def eventos_nexus(matriz,i,j):
    matriz[i][j] = '#'
   
    # print("i: ",i," j:",j)
   
    
    if(i==0 or i==10 or j==0 or j==49):
      return 1
    

    valor = 0
    if(matriz[i-1][j]=="+"): 
       valor += eventos_nexus(matriz,i-1,j)
        
    if(matriz[i+1][j]=="+"): 
        valor += eventos_nexus(matriz,i+1,j)

    if(matriz[i][j+1]=="+"): 
        valor += eventos_nexus(matriz,i,j+1)
  
    if(matriz[i][j-1]=="+"):   
        valor += eventos_nexus(matriz,i,j-1)
    
    if(matriz[i+1][j+1]=="+"):   
        valor += eventos_nexus(matriz,i+1,j+1)

    if(matriz[i+1][j-1]=="+"):   
        valor += eventos_nexus(matriz,i+1,j-1)

    if(matriz[i-1][j+1]=="+"):   
        valor += eventos_nexus(matriz,i-1,j+1)

    if(matriz[i-1][j-1]=="+"):   
        valor += eventos_nexus(matriz,i-1,j-1)
   
       

    return valor
    



def imprimir(ix,rta):
    print("Ramificacao {0}: {1} Eventos Nexus.".format(ix, rta))

# Leitura da matriz

matriz = []
for i in range(11):
  matriz.append(list(input()))


# for i in range(len(matriz)):
#   print(matriz[i])


for j in range(len(matriz[5])):
    if(matriz[4][j] == '+'):
        rta = eventos_nexus(matriz,4, j)
        imprimir(j,rta)
    elif(matriz[6][j] == '+'):
        rta = eventos_nexus(matriz,6, j)
        imprimir(j,rta)



# Deteção dos eventos nexus
# 