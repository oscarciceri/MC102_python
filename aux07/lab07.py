###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Vacinação AstraZeneca
# Nome: Oscar Jaime Ciceri Coral
# RA: 164786
###################################################

# Leitura dos dados

N = int(input())

vacinas = []

for x in range(N):
    vacinas.append(int(input()))

# print(vacinas)
# Listas dos números de vacinados com a primeira e segunda dose em cada mês

D1 = []
D2 = []

# Lista do número de vacinas devolvidas em cada mês

X = []

for i in range(N):
    D1.append(0)
    D2.append(0)
    X.append(0)

# Processamento dos dados
for i in range(N):
    auxvacinas=vacinas[i]
    if(i-3>=0):
        # print("1")
        if(D1[i-3]<vacinas[i]):
            D2[i]=D1[i-3]
        else:
            D2[i]=vacinas[i]
        # print(D1[i], " ", D2[i], "\n")
    vacinas[i]-=D2[i]
    if(i+3<N):
        # print("2")
        if(vacinas[i+3]>vacinas[i]):
            D1[i]=vacinas[i]
        else:
            D1[i]=vacinas[i+3]
         # print(D1[i], " ", D2[i], "\n")
    else:
        if(vacinas[i]>0):
            D1[i]=vacinas[i]
    vacinas[i]-=D1[i]   
   

    
    totalvacinas=D1[i]+D2[i]
    # print(totalvacinas)
    if(totalvacinas<auxvacinas):
        X[i]=auxvacinas-totalvacinas
    else:
        X[i]=0
    



    # print(D1[i], " ", D2[i], "\n")




# Impressão do uso das vacinas mês a mês

for i in range(N):
    print("Mes " + str(i+1) + ":")
    print("Vacinados com a primeira dose:", D1[i])
    print("Vacinados com a segunda dose:", D2[i])
    print("Vacinas devolvidas:", X[i])

# Impressão do resumo final
if(sum(D2)<sum(D1)):
    d1x=sum(D1)-sum(D2)
else:
    d1x=sum(D2)-sum(D1)

print("Total:")
print("Vacinados apenas com a primeira dose:",d1x)
print("Vacinados com as duas doses:", sum(D2))
print("Vacinas devolvidas:", sum(X))

