def minha_funcao(valor1, valor2):
    return valor1 + valor2


while True:
    valor_1 = int(input("Disgite o primeiro valor: "))
    valor_2 = int(input("Digite o segundo valor: "))
    
    resposta = minha_funcao(valor_1, valor_2)
    print("Resultado: ", valor_1, "+", valor_2, "=", resposta)
    break