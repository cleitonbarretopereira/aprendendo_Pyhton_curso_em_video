print('CÁLCULO DE SALÁRIO')
sal = float(input('Digite seu salário: '))
aumento = 0.10*sal
if sal <= 1250:
    aumento = 0.15*sal
print('Seu aumento foi de R$ {:.2f}, \nSeu novo salário é R${:.2f}'.format(aumento, (sal+aumento)))