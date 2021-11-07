matriz=[]
matrizlinha=input()
tamanho=len(matrizlinha)
z=0
g=0
while len(matrizlinha) == tamanho:
    matriz.append(matrizlinha)
    matrizlinha=input()
g=int(matrizlinha)
L=len(matriz)
C=len(matriz[0])
print(matriz)
print(g)


for z in range(g):
    print(z)
    print(g)
    x, y = [j for j in input().split()]
    print(x,y)
    #coordenada=list(map(int,input().split(" ")))
    #print(coordenada)