import math
print('SENO, COSSENO E TANGENTE')
angulo = float(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('Para o ângulo de {:.1f}º, o SENO é {:.2f}, o COSSENO é {:.2f}, e a TANGENTE é {:.2f}'.format(angulo, seno, cosseno, tangente))
