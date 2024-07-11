largura = float(input("digite o tamanho da largura: "))
altura = float(input("digite o tamanho da altura: "))

area = largura * altura

cobertura_tinta = 2.0

quantidade_necessaria = area / cobertura_tinta
print(f"Você precesará de {quantidade_necessaria:.3f} litros de tinta para pintar a parede.")


