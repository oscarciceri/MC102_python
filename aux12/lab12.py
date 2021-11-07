###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Busca em Imagens
# Nome: Oscar Ciceri
# RA: 164786
###################################################


                
def contido(A, B):
    flag = False
    i_max = len(A)-(len(B)-1)
    j_max = len(A[0])-(len(B[0])-1)
    for i in range(i_max):
        for j in range(j_max):
            if(A[i][j]==B[0][0]):
                x1 = i
                x2 = i+len(B)
                y1 = j
                y2 = j+len(B[0])
                sub = [sub[y1:y2] for sub in A[x1:x2]]
                if(sub==B):
                    flag = True

            if flag:
                break
        if flag:
            break
    if flag:
        return "Contido"
    else:
        return "Nao contido"

def flip_horizontal(B):
    max_fila_B = len(B)
    max_colum_B = len(B[0])
    Z = []
    valor = 0
    for i in range(max_fila_B):
        linha = []
        for j in range(max_colum_B):
            j_new = max_colum_B-j-1
            valor = B[i][j_new]
            linha.append(valor)
        Z.append(linha)
    return Z

def flip_vertical(B):
    max_fila_B = len(B)
    max_colum_B = len(B[0])
    Z = []
    for i in range(max_fila_B):
        linha = []
        for j in range(max_colum_B):
            i_new = max_fila_B-i-1
            valor = B[i_new][j]
            linha.append(valor)
        Z.append(linha)
    return Z

def rotacao_90(B):
    max_fila_B = len(B)
    max_colum_B = len(B[0])
    new_max_colum = max_fila_B
    new_max_fila = max_colum_B
    Z = []
    for i in range(new_max_fila):
        linha = []
        for j in range(new_max_colum):
            i_new = new_max_colum-j-1
            j_new = i
            valor = B[i_new][j_new]
            linha.append(valor)
        Z.append(linha)
    return Z

def imprimir(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

# leitura da imagem A
linhax0 = input() #P2 - linha a ser ignorada

max_colum_A, max_fila_A = [int(x) for x in input().split()]

linhax1 = input() #255 - linha a ser ignorada

A = []
for i in range(max_fila_A):
    linha = [int(x) for x in input().split()]
    A.append(linha)

# leitura da imagem B
linhax3 = input() #P2 - linha a ser ignorada

max_colum_B, max_fila_B = [int(x) for x in input().split()]

linhax4 = input() #255 - linha a ser ignorada

B = []
for i in range(max_fila_B):
    linha = [int(x) for x in input().split()]
    B.append(linha)



Zh = flip_horizontal(B)
Zv = flip_vertical(B)
Z90 = rotacao_90(B)
Z180 = rotacao_90(Z90)

# print('\nOriginal')
# imprimir(B)
# print('\nFlip_horizontal')
# imprimir(Zh)
# print('\nFlip_vertical')
# imprimir(Zv)
# print('\nRotacao_90')
# imprimir(Z90)
# print('\nRotacao_180')
# imprimir(Z180)

print("Original:",contido(A, B))
print("Flip horizontal:",contido(A, Zh))
print("Flip vertical:",contido(A, Zv))
print("Rotacao 90:",contido(A, Z90))
print("Rotacao 180:",contido(A, Z180))





