######################################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Vacinação CoronaVac
# Nome: Oscar Jaime Ciceri Coral	
# RA: 164786
######################################################################

# Leitura do número de meses


	

if __name__ == "__main__":
	


	n_meses = int(input())
	n_vacinas = []
	# Processamento de cada mês

	for x in range(n_meses):
		n_vacinas.append(int(input()))
	# Impressão da saída

	# print(n_meses)
	# print(n_vacinas)

	D2=0
	D1=0
	D2A=0
	D1A=0

	for x in n_vacinas:
		if(D1A>0 and x>0): # segunda_dose_em_atraso
			if(x>=D1A):
				D2A+=D1A
				D1A=0
			else:
				D2A+=x
				D1A-=x
		if(D1>0 and x>0): # segunda_dose_em_dia
			if(x>=D1):
				D2+=D1
				x-=D1
				D1=0
			else:
				D2+=x
				D1A+=D1-x
				D1-=x
				x=0
		if(x>0): # primeira_dose
			D1+=x

		if(D1A>D1):
			D1A=D1

		# print(D2)
		# print(D1)
		# print(D2A)
		# print(D1A,"\n")



	print("Pessoas completamente imunizadas:", D2)
	print("Pessoas imunizadas com uma dose:", D1)
	print("Pessoas com atraso na segunda dose:", D2A)
	print("Pessoas esperando segunda dose com atraso:", D1A)