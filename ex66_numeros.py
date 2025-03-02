valor = 0
cont = 0
while True:
    numeros = int(input('Digite valores (999 para parar): '))
    if numeros == 999:
        break
    else:
        valor = valor + numeros
        cont += 1
print(f'A soma dos {cont} valores informados é: {valor}')