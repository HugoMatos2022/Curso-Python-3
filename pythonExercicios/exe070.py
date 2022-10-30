totcompra = totmil = menor = cont = 0
barato = ''

print('Loja do Baratão')
print('*'*20)

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    totcompra += preco

    if preco >= 1000:
        totmil +=1

    if cont == 1 or preco < menor:
        menor = preco
        barato = produto


    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]

    if resp == 'N':
        break

print(f' O total da compra foi de R${totcompra:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O nome do produto mais barato é {barato} e ele custa {menor}')
print('Obrigado e volte sempre')
