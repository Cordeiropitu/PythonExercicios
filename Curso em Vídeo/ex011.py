l = float(input('Qual a largura da parede em metros? '))
a = float(input('Qual a altura da parede em metros? '))
area = l*a
ltinta = area/2

print('Você vai precisar de {} litros de tinta para pintar uma área de {} m²'.format(ltinta, area))