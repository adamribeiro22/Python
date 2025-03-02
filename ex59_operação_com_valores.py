n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
while True:
    opcao = int(input('Selecione uma opção: '
                      '1-Somar / 2-Multiplicar / 3-Maior / 4-Novos números / 5-Sair'))
    if opcao > 5 or opcao < 1:
        print('OPÇÃO INVÁLIDA: tente novamente')
    elif opcao == 1:
        soma = n1 + n2
        print(f'A soma é {soma}')
    elif opcao == 2:
        mult = n1 * n2
        print(f'O produto é {mult}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior número é {n1}')
        else:
            print(f'O maior número é {n2}')
    elif opcao == 4:
        print('informe novos números: ')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    else:
        print('Finalizando...')
        break