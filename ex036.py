print('COMPRA DE CASA')
salario = float(input('Digite seu salário: '))
valor = float(input('Valor da casa: '))
ano = (int(input('Em quantos irá financiar? ' )))
parcela = valor / (ano*12)

if parcela > (0.3*salario):
    print('Infelizmente seu financiamento NÃO foi aprovado.')
else:
    print('PARABÉNS, seu financiamento foi aprovado')
    print('Você pagará {} parcelas de R$ {:.2f}'.format((ano*12),parcela))
