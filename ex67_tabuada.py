while True:
    num = int(input('Digite um valor para a tabuada (digite qualquer número negativo para finalizar): '))
    if num < 0:
        break
    else:
        for c in range (1, 11):
            print(f'{num} x {c} = {num*c}')
print('Finalizado!')