###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Cartões de Crédito
# Nome: Oscar Jaime Ciceri Coral
# RA: 164786
###################################################




def nodo1():
	if(idade<50):
		nodo2()
	else:
		output("Cartao concedido")

def nodo2():
	if(salario<2000):
		nodo3()
	else:
		output("Cartao concedido")
	
def nodo3():
	if(saldo<5000):
		output("Cartao nao concedido")
	else:
		output("Cartao concedido")
	
def nodo4():
	if(idade<30):
		output("Cartao nao concedido")
	else:
		nodo5()

def nodo5():
	if(salario<3000):
		output("Cartao nao concedido")
	else:
		nodo6()

def nodo6():
	if(saldo<7000):
		output("Cartao nao concedido")
	else:
		output("Cartao concedido")


def output(text):
	print(text)


if __name__ == "__main__":
	# Leitura de dados
	score    = int(input())   
	idade    = int(input())   
	saldo    = float(input())   
	salario  = float(input())   


    
	# Verificação se o cartão de crédito será concedido ou não
	
	if(score>=600):
		nodo1()
	elif(score<300):
		output("Cartao nao concedido")
	else:
		nodo4()