

lista = ['P','A', 'Y', 'A', 'T', 'A', 'H', 'O', 'N']

#print(lista.count('A'))

for i in enumerate(lista):
    letra = i[1]
    #print(letra)

    if letra == 'A':
        lista.pop(i[0])
        print(lista)