print('ALISTAMENTO MILITAR')
ano = int(input('Digite o ano de nascimento: '))
idade = 2026-ano
if idade == 18:
    print('Você tem {} anos, está na hora de se alistar.'.format(idade))
elif ano == 2009:
    print('Você tem {} anos e falta {} ano para você se alistar.'. format(idade, 18-idade))
elif idade < 18:
    print('Você tem {} anos e ainda faltam {} anos para você se alistar.'. format(idade, 18-idade))
elif ano == 2007:
    print('Você tem {} anos e deveria estar alistado há {} ano.'.format(idade,(idade-18)))
elif idade > 18:
    print('Você tem {} anos e deveria estar alistado há {} anos.'.format(idade,(idade-18)))
