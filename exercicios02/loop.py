
container = []

for x in range(10):
    name_product = input("Nome do produto: ")
    price = float(input("preço: "))
    resultado = [name_product, price]
    container.append(resultado)
    print(container)


notas = []

contador = 1

while contador <= 5:
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)
    
    contador = contador + 1
    
print("Quantidade de notas", len(notas))

print("hello world")