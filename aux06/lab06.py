###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - O Porteiro do Castelo
# Nome: Oscar Jaime Ciceri Coral
# RA: 164786
###################################################

# Leitura de dados


sequencia = [int(i) for i in input().split()]

longitud=len(sequencia)
j=0
respuesta=False
while(respuesta==False and j<longitud):
	# print(sequencia)
	cont=0
	for i in range(len(sequencia)-1):
		if(sequencia[i]<sequencia[i+1]):
			cont+=1
	
	if(cont==len(sequencia)-1):
		respuesta=True


	aux=sequencia[0]
	for i in range(len(sequencia)-1):
		sequencia[i]=sequencia[i+1]
	sequencia[-1]=aux

	j+=1


if(respuesta==True):
	print("Klift, Kloft, Still, a porta se abriu")
else:
	print("Senha incorreta")

