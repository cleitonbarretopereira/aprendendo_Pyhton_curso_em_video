import random
print('APRESENTAÇÃO DE TRABALHO')
aluno1 = str(input('Primeiro Aluno(a): '))
aluno2 = str(input('Segundo Aluno(a): '))
aluno3 = str(input('Terceiro Aluno(a): '))
aluno4 = str(input('Quarto Aluno(a): '))
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
#print('{} foi o(a) sorteado().'.format(escolhido))
print('O trabalho será apresentado na seguinte ordem: {}'.format(lista))
