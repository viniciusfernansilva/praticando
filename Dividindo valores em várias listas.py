lista = []
lista_pares = []
lista_impares = []

while True:
    n = int(input('Digite um numero inteiro: '))
    lista.append(n)
    if n % 2 == 0:
        lista_pares.append(n)
    if n % 2 == 1:
        lista_impares.append(n)
    new = str(input('Deseja continuar? [S/N]')).upper()
    if new == 'S':
        continue
    if new == 'N':
        break
print(lista)
print(lista_pares)
print(lista_impares)
