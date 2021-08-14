fat = 1
x = 5
if type(x) is int:      #Caso o tipo da variável x seja inteiro
    while x > 0:        #Faça o looping enquanto ela for positiva
        fat *= x        #Multiplique o valor de x pela variável fat
        x -= 1          #Descresça x em uma unidade

print(fat)              #imprima o valor ao final do looping

