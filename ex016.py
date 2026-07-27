from math import trunc
print('***MOSTRANDO NÚMERO REAL***')
print('Resolução 1, usando o metodo TRUNC')
num = float(input('Digite um valor: '))
print('O número digitado foi {} e sua porção inteira é {}.'.format(num, trunc(num)))

print('-*-*'*13)

print('***Resolução 2, usando a opção INT***')
num2 = float(input(('Digite um número: ')))
print('O número digitado foi {}, e sua porção inteira é {}.'.format(num2, int(num2)))
