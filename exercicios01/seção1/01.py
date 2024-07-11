numberOne = int(input('digite seu numero: '))
numberTwu = int(input('digite outro numero: '))

s = numberOne+numberTwu
n = input('digite algo: ')
print('A soma entre {} e {} vale {}'.format(numberOne, numberTwu, s))
print('A soma dos números são: {}'.format (s)) 
print(n.isalpha())

#############################################
peso = int(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)

print('Seu IMC é: {}'.format(imc))

print('O tipo da variável imc é: {}\nO tipo da variável altura é: {}'.format(type(imc), type(altura)))

#############################################
number = int(input('digite um numero: '))
print('numero sucrssor: {} \n numero antecessor: {}'.format(number - 1, number + 1))

############################################
metro = int(input('Digite o valor em metro: '))
print('valor do metro em centíetros é: {}'.format(metro * 100))
print('valor do metro em milimetros é; {}'.format(metro * 1000))
