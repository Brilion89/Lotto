import random
from random import randint
item = ('Mega Sena', 'Loto Fácil', '+ Milionária')
mega = randint(1, 60)
#for mega in range(6):
facil = randint(1, 25)
#for facil in range(15):
milio = randint(1, 50) and randint(1, 6) * 2
#for milio in range(6):
print('''Vou gerar numeros aleatorios para o jogo que for escolhido:
[0] Mega Sena
[1] Loto Fácil
[2] + Milionária
''')
jogo = int(input('Selecione o jogo: '))
if jogo == 0:
    for mega in range(1, 7):
        print('Seu numeros aleatorios são: {}'.format(mega))
elif jogo == 1:
    for facil in range(1, 26):
        print('Seu numeros aleatorios são: {}'.format(facil))
else:
    print('Seu numeros aleatorios são: {}'.format(milio))
