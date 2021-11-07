def fatorial(n):
	print('n: ', n)
	if n == 0:
		return 1
	else:
		aux = fatorial(n - 1)

	print('\nn: ',n,' aux:',aux)
	x = n * aux
	print('x: ',x)

	return x

print("********** Examples **********\n")

print("Factorial\n")
valor  = 4 
f = fatorial(valor)
print('Rta: ', f)