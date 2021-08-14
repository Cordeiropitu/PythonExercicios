primo = [2]
prox_elemento = 2

while len(primo) <= 50:         # enquanto o comprimento da lista for menos do que 50 faça
    prox_elemento += 1          # some 1 na variavel de checagem dos números (prox_elemento)
    prox_elemento_status = ''   # variavel para armazenar valor para parar a divisão

    for elemento in primo:                          # elemento é uma unidade contida na lista primo
        quociente = prox_elemento / elemento        # divide o valor de teste pelo valor da lista primo
        quociente_int = prox_elemento // elemento   # salva o valor inteiro da divisão

        if quociente_int == quociente:              # se os valores das divisões forem iguais, ele não é primo
            prox_elemento_status = 'pula'           # adiciona o status pula
            break                                   # se o elemento for divisivel por algum da lista, quebramos o for

    if prox_elemento_status == 'pula':              # se receber a opção 'pula', a variavel volta para o while
        continue
    else:                                           # se não tiver a opção pula, ele armazena o número na lista de primos
        primo.append(prox_elemento)
print(primo)
print(len(primo))