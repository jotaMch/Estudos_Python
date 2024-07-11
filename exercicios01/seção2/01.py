from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a: {:.2f}'.format(num, raiz))


# Desafio: mostrar a parte inteira de um número real
numReal = float(input('Digite um numero real: '))
print('A parte inteira do numero real {} é: {}'.format(numReal, floor(numReal)))


# Biblioteca para gerar números aleatórios
import random
numRandom = random.randint(1, 20)
print('Número aleatório: ', numRandom)

print('\n<------------------------------------>\nFatiamento, Análise e Transformação abaixo:')
name = 'Antonio Jânderson'
# Fatiamento
print(name[8:])
print(name[12:16])
print(name[8::2])

# Análise
print(len(name))
print(name.count('o'))
print(name.count('o', 0, 7))  # Análisa apenas 'Antonio'
print(name.find('son'))  # Mstra a posição onde começa 'son'

# Transformação
print(name.replace('Antonio', 'Jânderson'))
print(name.lower())
print(name.upper())

