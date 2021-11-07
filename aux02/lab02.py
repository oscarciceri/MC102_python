###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Fórmula 1
# Nome: 
# RA: 
###################################################

# Leitura de dados

t  = float(input())           # tempo necessário para que o segundo colocado na corrida chegue até a saída dos boxes, em segundos (valor real).
dist_a = int(input())         # distância entre a entrada dos boxes e o local do pit stop, em metros (valor inteiro).
vel_a  = float(input())       # velocidade média para percorrer a distância entre a entrada dos boxes e o local do pit stop, em km/h (valor real).
t_pit_stop  = float(input())  # tempo gasto para realizar o pit stop, em segundos (valor real).
dist_b = int(input())         # distância entre o local do pit stop e a saída dos boxes, em metros (valor inteiro).
vel_b  = float(input())       #  velocidade média para percorrer a distância entre o local do pit stop e a saída dos boxes, em km/h (valor real).

# print(t)
# print(dist_a)
# print(vel_a)
# print(t_pit_stop)
# print(dist_b)
# print(vel_b)

vel_a_ms = vel_a*1000/3600  
vel_b_ms = vel_b*1000/3600  

# Cálculo do tempo total gasto para realizar o pit stop

t_total = (dist_a/vel_a_ms) + t_pit_stop + (dist_b/vel_b_ms)

# Impressão da resposta
if(t_total<t):
	print("True")
else:
	print("False")
