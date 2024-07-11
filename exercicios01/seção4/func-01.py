
def saudacao(nome, saudacao="Olá"):
    """Sauda uma pessoa com uma saudação."""
    print(f"{saudacao}, {nome}!")

saudacao("João")
saudacao("Maria", "Oi")

def soma_variavel(*args):
    """Soma todos os argumentos passados."""
    return sum(args)

resultado = soma_variavel(10, 20, 30, 40)
print(resultado)

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

resultado = fatorial(5)
print(resultado)

