import math
angulo = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))
print('O ângulo de {} tem o SENO de {}, COSSENO '
'de {} e TANGENTE {}'.format(angulo, seno, cos, tg))
