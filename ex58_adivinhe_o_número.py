from random import randint
cont = 0
numComp = randint(0,10)
while numComp:
    numUser = int(input('Tente adivinhar um número de 0 a 10: '))
    cont += 1
    if numUser != numComp:
        print('ERRADO, tente novamente! ')
        if numUser > numComp:
            print('Tente menos...')
        elif numUser < numComp:
            print('Tente mais...')
    else:
        print(f'VOCÊ ACERTOU! Tentou {cont} vezes.')
        break