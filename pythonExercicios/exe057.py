sexo = str(input('Informe seu sexo [M/F] ')).strip().upper()[0]  #strip() para tirar os espaços. upper()para passar tudo para maiusculo e [0]para fatiação e validaçao apenas da primeira letra
while sexo not in 'MnFf': # enquanto o sexo nao for M ou F ele cai no laço ate ser digitado corretamente
    sexo = str(input('Dados inválidos, por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
