p = int(input('Primeiro termo:'))
r = int(input('Razao: '))
decimo = p + (10 - 1) * r

for c in range (p, decimo+r, r):
    print(c, end='...')


