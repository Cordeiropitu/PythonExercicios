x = 'fdngjf'
if x is int:
    if x > 0:
        print('O número  {} é positivo'.format(x))
    elif x < 0:
        print('O número {} é negativo'.format(x))
    elif x == 0:
        print('O número vale ZERO')
else:
    print('Não é um número')