lista = []
while True:
    novo = int(input('Digite um numero inteiro: '))
    lista.append(novo)
    again = input('Deseja continuar? [S/N]').upper()
    if again == 'N':
        break
    else:
        continue

print(f'A lista tem {len(lista)} caracteres')
print(sorted(lista))
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O numero 5 não está na lista')
