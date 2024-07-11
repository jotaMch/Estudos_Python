nota1 = float(input('Qual sua primeira nota? '))
nota2 = float(input('Qual sua segunda nota? '))
nota3 = float(input('Qual sua terceira nota? '))

m = (nota1+nota2+nota3) / 3
mformat = round(m,1) # formatar em uma casa decimal
print('Sua média é {:.1f}'.format(m))

if mformat < 6:
    print('media ruim')
elif mformat >= 6:
    print('media boa')