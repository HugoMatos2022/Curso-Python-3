from datetime import date
atual = date.today().year
nasc = int(input('Qual o ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'. format(nasc, idade, atual))

print('''Digite o sexo
[1] Feminino
[2] Masculino''')

opção = int(input( 'Sua opção: '))

if opção == 1:
    print('Por ser do sexo Feminino o seu alistamento milítar não é obrigatório')

elif opção == 2 and idade == 18:
    print('Você tem que se alistar imediantamente')

elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta {} anos para seu alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento sera em {} ano'.format(ano))

elif idade > 18 :
    saldo = idade - 18
    print('Voce ja deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {} ano'.format(ano))
