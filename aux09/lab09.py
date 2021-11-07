#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Jogos Olímpicos
# Nome: 
# RA: 
#####################################################

# Leitura da primeira linha
N, Ox, Px, Bx = [int(x) for x in input().split()]
# print(N, Ox, Px, Bx)

# Leitura e processamento das provas
diccionario = {}

for i in range(N):
	tipo, p1, p2, p3 = [x for x in input().split()]

	if p1 in diccionario:
		valor = diccionario.get(p1)
		valor[0] += Ox 
		valor.append(tipo)
		diccionario[p1] = valor
	else:
		diccionario[p1] = [Ox, tipo]

	if p2 in diccionario:
		valor = diccionario.get(p2)
		valor[0] += Px  
		diccionario[p2] = valor
	else:
		diccionario[p2] = [Px]

	if p3 in diccionario:
		valor = diccionario.get(p3)
		valor[0] += Bx  
		diccionario[p3] = valor
	else:
		diccionario[p3] = [Bx]

# print(diccionario)




maximo = 0
for valor in diccionario.values():
	if(valor[0] > maximo):
		maximo = valor[0]
# print(maximo)


ordenados = []
for i in sorted (diccionario.keys()) :
	ordenados.append(i)

# print(ordenados)

for pais in ordenados:
	valor = diccionario.get(pais)
	if(valor[0] == maximo):
		print(pais, valor[0])
		for i in range(1,len(valor),1):
			print(valor[i])
	

# Impressão da saída