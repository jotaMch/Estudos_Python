import os
messagens = []

nome = input("Nome: ")

while True:
    os.system('cls')
    
    if len(messagens) > 0:
        for m in messagens:
            print(m['nome'], "-", m['texto'])
            
            
    print("_____________________")
    
    texto = input("mensagem: ")
    if texto == "fim":
        break

    messagens.append({
        "nome": nome,
        "texto": texto
    })