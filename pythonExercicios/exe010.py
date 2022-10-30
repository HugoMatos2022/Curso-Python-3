dinheiro = float(input('Quantos de dinheiro voce tem na carteira? R$'))
dolar = dinheiro / 3.27
euros = dinheiro / 5.08
print('Com R${:0.2f} voce pode comprar U${:0.2f}'.format(dinheiro, dolar))
print('Com R${:0.2f} voce pode comprar (E){:0.2f}'.format(dinheiro, euros))

