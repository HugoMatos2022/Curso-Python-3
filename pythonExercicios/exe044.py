print( '{:=^40}'.format(' Lojas Matos ') )
preco = float(input('Preço da compra : R$ '))

print(''' Condições de pagamentos
        [1] Á vista
        [2] Á vista no cartão 
        [3] 2x no Cartão
        [4] 3x ou mais no Cartão ''')

opcao = int(input('Qual a opção de pagamento? '))

if opcao == 1 :
    total = preco - (preco * 10 / 100)

elif opcao == 2 :
    total = preco - (preco * 5 / 100)

elif opcao == 3 :
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS '. format(parcela))

elif opcao == 4 :
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas pacelas vai ser? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS '.format(totalparc, parcela))
else:
    total = 0
    print('Opção inválida de pagamento, tente novamente')


print('Sua compra de R${:.2f} vai custar R${:.2f} no final. '.format(preco, total ))