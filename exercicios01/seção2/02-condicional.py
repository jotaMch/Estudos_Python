futuro = 'dinheiro saúde conhecimento trabalho casa'
futuroReal = futuro.split()

print(futuroReal[2][5])

youcar = int(input('Quantos anos tem o seu carro? '))

if youcar <= 3:
    print('You car is new')
else:
    print('You car is old')

print('\n<---------------------->\nNova condição')
idade = int(input('Qual sua idade? '))

print('Entrada autorizada' if idade >= 18 else 'Entrada somente com presença dos responsáveis')