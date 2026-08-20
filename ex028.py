from random import randint
from time import sleep

print('JOGO DE ADIVINHAÇÃO')
print('*--'*18)
comp = randint(1,10)
usuario = int(input('Pensei em um número de 1 a 10, adivinhe qual é: '))
print('Pensando...')
sleep(2)
print('*--'*18)
if comp==usuario:
    print('Parabéns, vc acertou, também pensei no {}.'.format(usuario))
else:
    print('Que pena, você errou. Eu pensei no {}.'.format(comp))
