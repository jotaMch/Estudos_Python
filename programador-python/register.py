pessoa = []

while True:
    decisao = int(input("digite 1 para cadastrar ou digite 2 para sair: "))
    if decisao == 2:
        print("Programa finalizado")
        break
    nome = input("Digite seu nome: \n")
    idade = int(input("Digite sua idade: \n"))
    pessoa.append({'Nome': nome, 'Idade': idade})

print(pessoa)