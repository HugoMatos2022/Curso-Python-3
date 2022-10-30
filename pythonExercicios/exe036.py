casa = float(input('Qual valor da casa que deseja financiar ?R$ '))
salario = float(input('Qual o valor do seu salario mensal ?R$ '))
anos = int(input('Em quantos anos deseja pagar a casa? '))
prestação = casa / (anos * 12) ## a prestação multiplica a quantidade de anos que o cliente quer pagar e divide pelo valor da casa, assim se tem o valor da prestçao
minimo = salario * 30 / 100
print('')
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f} '. format(casa, anos, prestação))

if prestação <= minimo:
    print('Empréstimo pode ser Aceito')
else:
    print('Empréstimo Negado')
