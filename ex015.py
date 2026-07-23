print('ALUGUEL DE CARROS')
km = float(input('Quantos KM o carro rodou? '))
dias = int(input('Por quantos dias ficou alugado? '))
custo_diaria = 60
custo_km = 0.15
print('Valor total a pagar: R$ {:.2f}.'.format((custo_diaria*dias)+(km*custo_km)))
