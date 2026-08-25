from time import sleep
print('NÚMERO MAIOR E NÚMERO MENOR')
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro Número: '))

if num1 > num2 and num1 > num3:
    maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

if num1 < num2 and num1 < num3:
    menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
print('Avaliando...')
sleep(2)
print('MAIOR NÚMERO = {} \nMENOR NÚMERO = {}'.format(maior, menor))
