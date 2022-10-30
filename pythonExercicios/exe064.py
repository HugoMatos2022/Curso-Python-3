n = int(input('Digite um numero [999 para sair do sistema ] :'))
cont = 0
soma = 0
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um numero [999 para sair do sistema ] : '))
print('Voce digitou {} números e a soma foi de {}'.format(cont, soma))
