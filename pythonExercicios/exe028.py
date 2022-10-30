from random import randint # importa o modulo randint da biblioteca random
from time import sleep
computador = randint(0,5) # escolha aleatórias entre os numeros escolhido
print('-*-' *30)
print('Vou pensar em números entre 0 e 10, tente me adivinhar')
print('-*-' *30)
jogador =   int(input('Em que número eu pensei? ')) # jogador tenta adivinhar o numero
print('Processando...')
sleep(3)
if jogador == computador:
    print('Ganhou')
else:
    print('Perdeu, eu pensei no numero {} e não no {}'. format(computador, jogador))






