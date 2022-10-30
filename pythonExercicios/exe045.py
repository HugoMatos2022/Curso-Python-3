from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções
[0] Pedra
[1] Papel
[2] Tesoura ''')
print('-=-=' *10 )

jogador = int(input('Qual é a sua jogada:'))
print('-='*10)

print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' *10)

if computador == 0 :
    if jogador == 0 :
        print('Empate')
    elif jogador == 1:
        print('Jogador Vence')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('Jogada inválida')

elif computador == 1 :
    if jogador == 0 :
        print('Computador Vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador vence ')
    else:
        print('Jogada inválida')

elif computador == 2 :
    if jogador == 0 :
        print('Jogador Vence')
    elif jogador == 1:
        print('Computador Vence')
    elif jogador == 2:
        print('Empate ')
    else:
        print('Jogada inválida')


