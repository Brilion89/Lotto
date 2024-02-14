from random import sample
from time import sleep
import emoji
item = ('Mega Sena', 'Loto Fácil', '+ Milionária')
mega = list(range(1, 61))
m1 = sample(mega, 6)
facil = list(range(1, 26))
f1 = sample(facil, 15)
milio = list(range(1, 60))
m1 = sample(milio, 6)
print(emoji.emojize(''':dollar_banknote: Vou gerar numeros aleatorios para o jogo que for escolhido :dollar_banknote: :
[0] \033[4;30;44mMega Sena\33[m
[1] \033[4;30;41mLoto Fácil\33[m
[2] \033[4;30;43m+ Milionária\33[m
[3] \033[4;30;47mCancelar\033[m
''', language='alias'))
jogo = int(input('Selecione o jogo: '))
if jogo == 0:
    print('\033[4;30;44mSeu numeros aleatorios Mega-Sena são: {}\033[m'.format(m1, sleep(1)))
elif jogo == 1:
    print('\033[4;30;41mSeu numeros aleatorios Loto-Fácil são: {}\033[m'.format(f1, sleep(1)))
elif jogo == 2:
    print('\033[4;30;43mSeu numeros aleatorios + Milionária são: {}\033[m'.format(m1, sleep(1)))
else:
    print('\033[4;30;47mPrograma encerrado com sucesso.\033[m')
