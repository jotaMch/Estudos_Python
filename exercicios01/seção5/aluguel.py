dias = int(input("quantidade de dias alugados? "))
km = float(input("Quantos km rodados? "))

pago = (dias * 60) + (km * 0.15)
print(f"O valor total a pagar é {pago:.2f}")
