num = int(input("Informe um número: "))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"{num}\n\n A unidade é {u}, a dezena é {d}, a centena é {c}, a milhar é {m}")

