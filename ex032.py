print('ANO BISSEXTO')
ano = int(input('Digite um ano para ver se ele é BISSEXTO: '))
if ano%4 == 0 and ano %100 != 0 or ano %400 == 0:
    print('O ano {} É BISSEXTO.'.format(ano))
else: 
    print('O ano {} NÃO é BISSEXTO.'.format(ano))