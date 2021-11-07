###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Avatar
# Nome: Oscar Jaime Ciceri Coral	
# RA: 164786
###################################################

# Inicialização das variáveis

water = 0
earth = 0
fire = 0
air = 0


# Leitura da sequência de treinamento
tipo = input()

while(tipo!="X"):
	valor = int(input())
	# print(tipo)
	# print(valor)
	valor2=valor/2
	if(tipo=="W"):
		water+=valor
		if(fire-valor2<0):
			fire=0
		else:
			fire-=valor2
	elif(tipo=="F"):
		fire+=valor
		if(water-valor2<0):
			water=0
		else:
			water-=valor2
	elif(tipo=="E"):
		earth+=valor
		if(air-valor2<0):
			air=0
		else:
			air-=valor2
	else:
		air+=valor
		if(earth-valor2<0):
			earth=0
		else:
			earth-=valor2
	tipo = input()






# Impressão das informações de saída

print("Pontuacao Final")
print("Agua: {:.1f}".format(water))
print("Terra: {:.1f}".format(earth))
print("Fogo: {:.1f}".format(fire))
print("Ar: {:.1f}".format(air))

if(water>0 and fire>0 and earth>0 and air>0):
	print("Treinamento realizado com sucesso.")
else:
	print("Realize mais treinamentos.")
