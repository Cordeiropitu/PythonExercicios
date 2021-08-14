# > Maior
# < Menor
# = Atribuição
# == Igual
# += Soma o valor a direita pelo da esquerda
# *= Multiplica o valor a direita pelo da esquerda
# != Diferente
# >= Maior e igual
# <= Menor e Igual


x = 5

if type(x) is str:
    print('Impossivel realizar operação')

elif type(x) is not str:
        if x > 0:
            print('Positivo')
        elif x < 0:
             print('Negativo')
        #else:
        #print('Nenhuma alternativa')


# LOOP FOR
#
# range: seus elementos são inteiros; conta a quantidade de elementos
# list: seus elementos são os que estão contidos na lista
# enumerante: seus elementos são tuplas que contém inteiros e valores

lista = ['a', 2, 'b', 4, 5]
for i in lista:
    print(i)

for i in range(len(lista)):
   print(i)

#for i in enumerate(lista):
 #   print(i[1])


# LOOP WHILE
#
# continua executando uma ação enquanto ela for veraddeira

x = 10
while x > 7:
    print(x)
    x += 1
    if x > 20:
        break