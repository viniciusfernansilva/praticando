notas = []
while True:
    nome = str(input('Digite seu nome: '))
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    notas.append([nome, [nota_1, nota_2], media])
    novo = input('Deseja adicionar um novo aluno? [S/N]').upper()
    if novo == 'N':
        break
print('=' *30)
print(f'{"No.":.<4}{"NOME":.<10}{"MEDIA":.>8}')
print('-' *26)
for i, a in enumerate(notas):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

print('=*=' *12)
while True:
    ind = int(input('Deseja ver a nota de qual aluno? (999 para terminar) '))
    if ind == 999:
        break
    if ind <= len(notas) - 1:
        print(f'As notas de {notas[ind][0]} foram: {notas[ind][1]}')