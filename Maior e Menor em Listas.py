valores = []

for i in range(5):
    novo = float(input('Digite um valor numérico: '))
    valores.append(novo)


print(f'O maior valor listado foi: ', end='')
print(max(float(valor) for valor in valores))
print(f'O menor valor listado foi: ', end='')
print(min(float(valor) for valor in valores))