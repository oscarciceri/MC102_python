###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Fuga de Nova York
# Nome: 
# RA: 
###################################################

# Leitura da matriz
# DICA: o método isnumeric() pode ser útil para determinar o fim da leitura da matriz 


def salida(x,y):
	i=x
	j=y

	maxFilas = len(matriz)-1
	maxColum = len(matriz[0])-1
	# print(i,j)
	flag=False

	m = [linha[:] for linha in matriz]
	while(flag==False):

		# print(i,j)

		if(m[i][j]=='N'):
			m[i][j] = 'X'
			i-=1
		elif(m[i][j]=='S'):
			m[i][j] = 'X'
			i+=1
		elif(m[i][j]=='L'):
			m[i][j] = 'X'
			j+=1
		elif(m[i][j]=='O'):
			m[i][j] = 'X'
			j-=1
		elif(m[i][j]=='X'):
			print("Resgate aereo solicitado.")
			flag=True

		# print(m[0])
		# print(m[1])
		# print(m[2])
		# print(m[3])
		# print(m[4])
		# print(m[5])
		# print(m[6])
		# print(m[7])

		if(i>maxFilas):
			print("Fuga pelo sul.")
			flag=True
		elif(i<0):
			print("Fuga pelo norte.")
			flag=True
		elif(j>maxColum):
			print("Fuga pelo leste.")
			flag=True
		elif(j<0):
			print("Fuga pelo oeste.")
			flag=True



		


# Leitura das coordenadas e início do processamento
matriz = []
numero = 0
flagx = True
while(flagx==True):
	entrada = input()
	# print(entrada)

	if(entrada[0]=='N' or entrada[0]=='S' or entrada[0]=='L' or entrada[0]=='O'):
		numero = len(entrada)
		aux = []
		impar = True
		for i in range(numero):
			if(impar==True):
				aux.append(entrada[i])
				impar=False
			else:
				impar=True
		matriz.append(aux)
	else:
		flagx = False
		numero=int(entrada)
	

	


# print(len(matriz[-1]))

# print(matriz)
# matriz.pop(-1)
tamanho = numero
# print(matriz)
# print(tamanho)

pos = []
for i in range(tamanho):
	x, y = [j for j in input().split()]
	pos.append((int(x),int(y)))
# print(pos)


aux = []
for i in range(tamanho):
	aux = pos[i]
	x = int(aux[0])
	y = int(aux[1])
	salida(x,y)





