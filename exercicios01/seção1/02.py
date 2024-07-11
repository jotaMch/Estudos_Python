peso = int(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

# Cálculo correto do IMC
imc = peso / (altura ** 2)

print('Seu IMC é: {}'.format(imc))

# Corrigindo a formatação da string
print('O tipo da variável imc é: {}\nO tipo da variável altura é: {}'.format(type(imc), type(altura)))
