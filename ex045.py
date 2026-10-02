print('JO KEN PÔ')
from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint (0, 2)

print('''
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input('FAÇA SUA JOGADA: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

print('='*24)
print('O computador jogou {}'.format(itens[computador]))
print('Você jogou {}.'.format(itens[jogador]))
print('='*24)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('PARABÉNS, VOCÊ GANHOU')
    elif jogador == 2:
        print('O COMPUTADOR GANHOU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('O COMPUTADOR GANHOU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('PARABÉNS, VOCÊ GANHOU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('PARABÉNS, VOCÊ GANHOU.')
    elif jogador == 1:
        print('O COMPUTADOR GANHOU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
