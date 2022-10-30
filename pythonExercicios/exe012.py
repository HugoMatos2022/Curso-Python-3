produto = float(input('Qual o preço do produto? R$'))
desconto = produto - (produto * 5 / 100)
print('O produto que custava R${} na promoção com desonte de 5% vai custar R${:0.2f}'.format(produto, desconto))

