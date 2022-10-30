r1 = float(input('Primeiro segmwnto: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 :
    print('Os segmentos acima podem formar um triângulo', end=' ')
    if r1 == r2 == r3 :
        print('Equilátero') # Todos lados iguais
    elif r1 != r2 != r3 != r1 :
        print('Escaleno') # Todos os lados diferentes
    else:
        print('Isósceles') # Dois lados iguais

else:
    print('Os segmentos acima não podem formar um triângulo: ')
