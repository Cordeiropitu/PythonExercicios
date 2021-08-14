valores = [1, 2, 3, 4, 5]
keys = ['a', 'b', 'c', 'd', 'e']

#for i in range(5):
#    dicionario = {valores[i]: keys[i]}
#    print(dicionario)


dict_1 = {}
for i in range(5):
    dict_1[keys[i]] = valores[i]
    print(dict_1)

dict_3 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
valores = list(dict_3.values())
keys = list(dict_3.keys())
print(valores)
print(keys)