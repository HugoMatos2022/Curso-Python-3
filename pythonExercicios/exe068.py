from random import randint
v = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('Voce quer ser par ou Impar [P-I]: ')).upper()[0]
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {total}')

    if tipo == 'P':
        if total % 2 == 0:
            print(f'Voce venceu')
            v += 1
        else:
            print('Voce perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print(f'Voce venceu')
            v += 1
        else:
            print('Voce perdeu')
            break
    print('-'*10)
    print('Vamos jogar novamente...')
print(f'Gamer Over, Voce venceu {v} vezes')

