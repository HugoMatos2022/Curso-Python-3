largura = float(input('Qual a largura da parede: '))
altura = float(input('Qual a altura da parede: '))
area = largura * altura
print('Sua parede tem a dimensão de {}x{} e sua area é de {:0.2f}m²'.format(largura, altura, area))
tinta = area / 2
print('Voce vai precisar de {:0.2f}L. para sua obra'.format(tinta ))



