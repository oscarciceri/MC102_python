###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Ordenação de Panquecas
# Nome: Oscar Ciceri
# RA: 164786
###################################################

# Dada uma sequência de números de inteiros, gera
# uma string representando a pilha de panquecas
def str_panquecas(lista):
  return(" ".join(map(str, lista)))


def encontrar(lista, n):
  mayor = 0
  pos = 0
  flag = False
  for i in range(len(lista)-n):
    if(lista[i]>mayor):
      mayor = lista[i]
      pos = i

  if(pos == len(lista)-n-1):
    flag = True
  return pos+1, flag

def invertir(lista, pos):
  i = 0 
  j = pos 
  aux = lista[:pos]
  aux.reverse()
  for i in range(pos):
    lista[i]=aux[i]

  return lista

def estan_ordenados(lista):
  numero = lista[0]
  ordenados = True
  for i in range(1,len(lista)):
    if(numero<lista[i]):
      numero = lista[i]
    else:
      ordenados = False
      break
  return ordenados




lista = [int(x) for x in input().split()]
# print(lista)

if(estan_ordenados(lista)):
  print('Panquecas ja ordenadas')
else:
  for i in range(len(lista)):
    pos, flag = encontrar(lista, i)
    if flag == False:
      print("Posicionando a panqueca", lista[pos-1])
      if(pos!=1):
        lista = invertir(lista, pos)
        print("Primeira inversao:",str_panquecas(lista))

      lista = invertir(lista, len(lista)-i)
      print("Segunda inversao:",str_panquecas(lista))


