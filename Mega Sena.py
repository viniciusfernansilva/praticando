from random import randint
numeros_mega = []
jogos = []
qtd = int(input('Digite a quantidade de jogos a ser feito: '))
total = 0
while total < qtd:
    contador = 0
    while True:
        num = randint(1, 60)
        if num not in numeros_mega:
            numeros_mega.append(num)
            contador += 1
        if contador >= 6:
            break

    numeros_mega.sort()
    jogos.append(numeros_mega[:])
    numeros_mega.clear()
    total += 1

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')



