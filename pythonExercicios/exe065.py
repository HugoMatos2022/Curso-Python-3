resp = 's'
soma = quant = media = maior = menor = 0
while resp == 'Ss':
    num = int(input("Digite um número: "))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
media = soma / quant

print('Voce digitou {} números e a média foi de {} '.format(quant, media))
print('O maior numero foi {} e o menor foi de {} '.format(maior, menor))


