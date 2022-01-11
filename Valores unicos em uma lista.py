lista_numeros = []

for i in range(5):
    novo = int(input('Digite um numero: '))
    if i == 0 or novo > lista_numeros[-1]:
        print('Numero adicionado a lista')
        lista_numeros.append(novo)
    else:
        pos = 0
        while pos <= len(lista_numeros):
            print('Numero adicionado ao inicio da lista')
            lista_numeros.insert(pos, novo)
            break
        pos += 1

print(lista_numeros)