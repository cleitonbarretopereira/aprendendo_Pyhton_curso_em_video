print('CALCULANDO DESCONTO')
valor = float(input('Digite o valor do produto: '))
aumento = 0.05
print('O aumento é de R$ {:.2f} e o novo valor de venda é R$ {:.2f}'.format(valor*aumento,valor+(valor*aumento)))
