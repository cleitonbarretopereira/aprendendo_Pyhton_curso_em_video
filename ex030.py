from time import sleep
print('PAR OU IMPAR')
num = int(input('Digite um número: '))
num2 = num%2
print('Analizando...')
sleep(2)
if num2 == 0:
    print('O número digitado é PAR.')
else:
    print('O número digitado é IMPAR.')