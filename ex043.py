print('CÁLCULO DE IMC')
alt = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (alt*alt) 

if imc < 18.5:
    print('Abaixo do Peso')
elif imc >18.5 and imc <= 25:
    print('Peso Ideial')
elif imc > 25 and imc <= 30:
    print('Sobre Peso')
elif imc > 30 and imc <= 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade Mórbida')

print('IMC = {:.2f}'.format(imc))