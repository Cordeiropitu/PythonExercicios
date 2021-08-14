letras = ['a', 'r', 'a', 'r', 'a']
x = len(letras)
y = letras.count('a')
z = letras.count('r')
palavras = []
iteracoes: 0

for i5 in range(len(letras)):                   # para um elemento i5 na sequencia do comprimento de letras
    L5 = letras[i5]                             # armazena os valores da lista letras na variavel l5
    lista_L5 = letras.copy()                    # copia a lista de letras para a lista L5
    lista_L4 = lista_L5.copy()                  # copia a lista_l5 para a lista l4
    lista_L4.pop(i5)                            # remove a primeira letra da lista  l4
                                                # pop() sem paramentro remove o ultimo elemento da lista

    for i4 in range(len(lista_L4)):
        L4 = lista_L4[i4]
        lista_L3 = lista_L4.copy()
        lista_L3.pop(i4)

        for i3 in range(len(lista_L3)):
            L3 = lista_L3[i3]
            lista_L2 = lista_L3.copy()
            lista_L2.pop(i3)

            for i2 in range(len(lista_L2)):
                L2 = lista_L2[i2]
                lista_L1 = lista_L2.copy()
                lista_L1.pop(i2)

print(L2)

