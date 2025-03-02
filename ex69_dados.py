cont_idade = 0
cont_homem = 0
cont_mulher_20 = 0
while True:
    print('CADASTRO')
    idade = int(input('Digite sua idade: '))
    if idade > 18:
        cont_idade += 1
    sexo = input('Digite seu gênero (M/F: ').upper()
    if sexo == 'M':
        cont_homem += 1
    if sexo == 'F' and idade < 20:
        cont_mulher_20 += 1
    resp = input(('Quer continuar? (S/N) ')).upper()
    if resp == 'N':
        break
print(f'Há {cont_idade} pessoas com mais de 18 anos')
print(f'Há {cont_homem} homens')
print(f'Há {cont_mulher_20} mulheres com menos de 20 anos')