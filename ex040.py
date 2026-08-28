print('CÁLCULO DE MÉDIA')
n1 = float(input('Nota 1: '))
n2 = float (input('Nota 2: '))
media = (n1+n2)/2
if media < 5:
    print('Sua Média foi {}, você foi REPROVADO.'.format(media))
elif media >= 5 and media <= 6.9:
    print('Sua Média foi {}, você está em RECUPERAÇÃO.'.format(media))
else:
    print('Sua Média foi {}, você foi APROVADO, parabéns.'.format(media))
