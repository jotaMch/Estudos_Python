def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

resultado = fatorial(5)
print(resultado)

def textToUpper(texto):
    if texto.islower():
        return texto.upper()
    else:
        return texto

entrada = input("Digite um texto: ")
resultado = textToUpper(entrada)
print("Resultado:", resultado)
