temp = float(input('Informe a temperatura em Cº:'))
celsius = ( temp * 1.8) + 32
print('A temperatura de Celsius para fahrenheit é {}'.format(celsius))

temp2 = float(input('Informe a temperatura em F:'))
f = (temp2 - 32) / 1.8
print('A temperatura em fahrenheit para celsius é {:.2f}'.format (f))