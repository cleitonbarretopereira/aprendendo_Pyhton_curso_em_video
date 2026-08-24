print('RADAR ELETRÔNICO')
multa = 0
velocidade=float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print('Você ultrapassou o limite de velocidade')
    print('Você foi multado em R$ {}.'.format(multa))
else:
    print('Boa viagem')
    
