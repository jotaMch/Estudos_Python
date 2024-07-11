from random import randint
from time import sleep
computador = randint(0, 5)
print('== '* 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('== ' * 20)
jogador = int(input("Em que numero eu pensei? "))
print('PROCESSANDO...')

sleep(2)

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! eu pensei no número {} e não no número {}'.format(computador, jogador))


# metodo split e laço for 
    print('\n\nMetodo split e laço for, carregando ...')
sleep(4)

alimento = 'batata carne arroz feijão'
comida = alimento.split()

for p in comida:
    print(p)

tarefas = ['dormir', 'acordar']
lista = ['limpar', 'organizar', 'analisar', 'avançar', 'procurar', 'resolver', 'praticar', 'realizar', 'nome', 'email', 'telefone', 'endereço']

for success in tarefas:
    print(f'itens da lista: {success}')

if  len(tarefas) < 4:
    print(tarefas)
    novo_item = input("Digite um novo item para adicionar à lista de tarefas: ")
    tarefas.append(novo_item)
    print(tarefas)
