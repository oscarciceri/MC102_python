###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Emparelhamento de Primers
# Nome: 
# RA: 
###################################################

# Leitura de dados
fita  = input() 
primer = input() 

# Verificação da ligação dos primers na fita
primerx = "5"
for value in primer:
	if(value == "A"):
		primerx =  primerx + "T"
	elif(value == "T"):
		primerx =  primerx + "A"
	elif(value == "G"):
		primerx =  primerx + "C"
	elif(value == "C"):
		primerx =  primerx + "G"
primerx =  primerx + "3"

primerx = primerx[::-1]
primerx = primerx[1:len(primerx)-1:1]

aux = False
auxpos = 0
matches = []
while(aux == False):
	pos =(fita.find(primerx))
	if(pos == -1):
		aux = True
	else:
		matches.append(pos + auxpos)
		fita = fita[pos+1:len(fita)-1:1] 

for i in range(1,len(matches)):
	matches[i] = matches[i]+ matches[i-1] + 1

if(len(matches)==0):
	print("Nenhuma ligacao")
else:
	for valor in matches:
		print("Ligacao na posicao",valor)


# Impressão da saída do programa