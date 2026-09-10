print('COMPARAÇÃO DE NÚMERPS')
num1 = int(input('Primeiro Número: '))
num2 = int(input('Segundo Número: '))

if num1 > num2:
    print('Maior{}'.format(num1))
    print('Menor{}'.format(num2))
elif num1 < num2:
    print('Maior{}'.format(num2))
    print('Menor{}'.format(num1))
else:
    print('Os números são iguais.')
    