lista = [(2*i+1) for i in range(20)]
print(lista)

f_x = lambda x:(x*2 + 1)
lista_impar_2 = [f_x(x) for x in range(20)]
print(lista_impar_2)

