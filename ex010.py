din = float(input('Quanto de dinheiro você tem na carteira? R$:'))
dolar = din * 5.88
euro = din * 6.61
print('Com {} reais, você compra {:.2f}USD, {:.2F}euro'.format(din,dolar,euro))