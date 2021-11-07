###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - Fuga de Nova York II
# Nome: Oscar Ciceri  
# RA: 164786  
###################################################



# Dada uma matriz e a posição (x,y), realiza a 
# verificação de é possível realizar a fuga da cidade
# ou se é necessário o resgate aéreo.

def fuga(m, i, j):
  maxFilas = len(m)-1
  maxColum = len(m[0])-1

  # print("i: ",i," j:",j)

  flag = False

  if(m[i][j] == "N"):
    flag = False
  else:
    if(i+1>maxFilas or i-1<0 or j+1>maxColum or j-1<0):
      # print("True")
      flag=True
 
    if(flag==False):
      if(m[i][j]=='H'):
        m[i][j] = '#'
        flag = fuga(m, i, j+1)
        if(flag==False):
          flag = fuga(m, i, j-1)

      elif(m[i][j]=='V'):
        m[i][j] = '#'
        flag = fuga(m, i+1, j)
        if(flag==False):
          flag = fuga(m, i-1, j)

      elif(m[i][j]=='T'):
        m[i][j] = '#'
        flag = fuga(m, i, j+1)
        if(flag==False):
          flag = fuga(m, i, j-1)
        if(flag==False):
          flag = fuga(m, i+1, j)
        if(flag==False):
          flag = fuga(m, i-1, j)
      else:
        # print("False:",m[i][j])
        flag = False

  return flag



# Leitura de dados
matriz = []    
linha = input()
while not(linha.isnumeric()):
  matriz.append(linha.split())
  linha = input()
n = int(linha)


# for i in range(len(matriz)):
#   print(matriz[i])
# print(n)



# Verifica se é preciso realizar a fuga da cidade
# ou solicitar o resgate aéreo para cada posição

for x in range(n):
  i, j = [y for y in input().split()]
  ii = int(i)
  jj = int(j)

  # print(i,j)
  m = [linha.copy() for linha in matriz]
  rta = fuga(m, ii, jj)


  if(rta):
    print("Fuga da cidade realizada.")
  else:
    print("Resgate aereo solicitado.")



#3
# Fuga da cidade realizada.
# Resgate aereo solicitado.
# Fuga da cidade realizada.
# Fuga da cidade realizada.
# Fuga da cidade realizada.
# Resgate aereo solicitado.
# Fuga da cidade realizada.
# Resgate aereo solicitado.
# Fuga da cidade realizada.
# Fuga da cidade realizada.
#8
# Resgate aereo solicitado.
# Resgate aereo solicitado.
