from time import sleep
print('CÁLCULO DE VIAGEM')
km = float(input('Digite a distância da viagem: '))
print('Calculando...')
sleep(2)
if km> 200:
    custo = 0.45*km
else:
    custo = 0.50*km
print('Para sua viagem de {:.2f}Km, o preço da passagem será de R$ {:.2f}. \nBoa Viagem!'.format(km, custo))
