brasileirao = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco', 'Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude', 'Bragantino', 'Athletico', 'Criciúma', 'Atlético-GO', 'Cuiabá')

print(f'Os 5 primeiros são: {brasileirao[0:5]}')

print(f'Os 4 últimos são: {brasileirao[16:]}')

print(f'Os times em ordem alfabética: {sorted(brasileirao)}')

print(f'O Vasco da Gama está em {(brasileirao.index('Vasco'))}º lugar.')