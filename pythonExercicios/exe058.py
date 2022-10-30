from random import randint

computador = randint(0,10)
print('Sou o seu computador...Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi? ')

acertou = False # inicia a variavel com falso porque ela ainda nao acertou
palpites = 0

while not acertou: # enquanto ele nao acertou
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez')
        elif jogador > computador:
            print('Menos...tente mais uma vez ')
print('Acertou com {} tentativas. Parabéns'.format(palpites))

