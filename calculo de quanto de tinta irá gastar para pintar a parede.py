largura = float(input('Digite a largura da sua parede: '))
altura = float (input('Digite a altura da sua parede: '))
area = largura * altura
print('A sua parede tem dimensão de {}x{} e sua area é de {:.2f}m²'.format(largura, altura, area))
tinta = area / 2
print('para pintar essa parede, você precisará de {}'.format (tinta))
