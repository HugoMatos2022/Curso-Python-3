distancia = int(input('Qual a distancia da sua viagem? '))
print('Você está preste a começar uma viagem de {}KM sente-se confortável. '. format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço da sua passagem vai ser de R${}'. format(preco))
