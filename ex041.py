from datetime import date
print('CATEGORIA DE NADADORES')

ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year-ano

if idade <= 9:
    print('Mirim')
elif idade > 9 and idade <= 14:
    print('Infantil')
elif idade > 14 and idade <= 19:
    print('JÚNIOR')
elif idade > 19 and idade <=24:
    print('SÉNIOR')
elif idade >= 25:
    print('MASTER')

print('{} anos.'.format(idade))
'''Achar jeito de contar os 4 digitos da variavel ANO e retornar msg de erro caso o usuário não digite 4 numeros'''
