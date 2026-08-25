from time import sleep
print('*--'*8)
print('RADAR ELETRÔNICO')
print('*--'*8)
velocidade=float(input('Digite a velocidade do carro: '))
multa = velocidade-80

if velocidade > 80:
    print('Calculando...')
    sleep(3)
    print('Você ultrapassou o limite de velocidade')
    print('Calculando multa...')
    sleep(2)
    print('Você foi multado em R$ {:.2f}.'.format(multa*7))
else:
    print('Calculando...')
    sleep(3)
    print('Você está dentro do limite de velocidade. \nBoa viagem!')
