dias = float(input('Quantos dias o carro ficará alugado? '))
km = float(input('Quantos Km rodados? '))
total = (dias * 60) + (km * 0.15)
print('Total a pagar: {}'.format(total))