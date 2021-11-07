N, O, P, B = [int(x) for x in input().split()]
paises={}
Modalidade={}
lista=[]
ouro=0
prata=0
bronze=0
pontuacao=[]
for a in range(0,N):
    (modalidade, pais_ouro, pais_prata, pais_bronze)=input().split()
    if pais_ouro not in paises:
        paises[pais_ouro]=0
    if pais_prata not in paises:
        paises[pais_prata]=0
    if pais_bronze not in paises:
        paises[pais_bronze]=0
    if pais_ouro in Modalidade:
        Modalidade[pais_ouro]+='\n{}'.format(modalidade)
    else:
        Modalidade[pais_ouro]=modalidade


    paises[pais_ouro]+=O
    paises[pais_prata]+=P
    paises[pais_bronze]+=B
os_paises=list(paises.keys())
pontuacao_dos_paises=paises.values()
melhor_pontuacao=max(pontuacao_dos_paises)
def get_key(val):
    for key, value in paises.items():
         if val == value: 
             lista.append(key)
get_key(melhor_pontuacao)
lista.sort()
for a in lista:
    valor = paises.get(a)
    print(a, valor)
    esportes = Modalidade.get(a)
    if(esportes!=None):
        print(esportes)
