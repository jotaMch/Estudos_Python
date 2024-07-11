from math import trunc, radians, sin, cos, tan
num = float(input('Digite um numero: '))
print(f'O valor digitado foi {num} e a sua porção inteira é {trunc(num)}')



angulo= float(input("Digite o ângulo que você  deseja: "))
seno= sin(radians(angulo))
cosseno= cos(radians(angulo))
tangente= tan(radians(angulo))

print(f"O ângulo de {angulo:} tem o seno de {seno:.2}\n, "
      f"tem o cosseno de {cosseno:.2} e a tangente de {tangente:.2}")
