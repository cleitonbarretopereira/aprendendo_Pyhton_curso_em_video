import random
print('SORTEANDO ALUNO')
aluno1 = str(input('Primeiro Aluno(a): '))
aluno2 = str(input('Segundo Aluno(a): '))
aluno3 = str(input('Terceiro Aluno(a): '))
aluno4 = str(input('Quarto Aluno(a): '))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print('{} foi o(a) sorteado().'.format(escolhido))
