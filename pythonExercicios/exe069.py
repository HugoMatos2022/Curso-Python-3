tot18 = totalh = totm20 = 0
while True:
    print('Cadastre uma pessoa')
    print('-'*20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF' :
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]

    if idade >= 18:
            tot18 += 1
    if sexo == 'M':
            totalh += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1


    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N':
        break
print('*'*20)
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'ao todo temos {totalhh} homens cadastrados')
print(f'E temos {totm20} mulheres com 20 anos')

