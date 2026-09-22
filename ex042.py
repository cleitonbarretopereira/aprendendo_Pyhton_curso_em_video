print('ANALISANDO TRIÂNGULOS 2.0')
seg1 = float(input('Segmento 1: '))
seg2 = float(input('Segmento 2: '))
seg3 = float(input('Segmento 3: '))
if seg1 < seg2+seg3 and seg2 < seg1+seg2 and seg3 < seg1+seg2:
    if seg1 == seg2 and seg2 == seg3 and seg1 == seg3:
        tipo = 'EQUILATERO'
    elif seg1 != seg2 and seg1 != seg3 and seg2 != seg3:
        tipo = 'ESCALENO'
    else: 
        tipo = 'ISÓSCELES'
        print('Forma triângulo {}.'.format(tipo))
else:
    print('Não forma triângulo')
