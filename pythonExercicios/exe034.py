salario = float(input('Qual o salário do funcionário? R$'))

if salario <= 1250:
    novoSal = salario + (salario * 15 / 100)
else:
    novoSal = salario + (salario * 10 / 100)
print('O novo salário do colaborador é de R${}'.format(novoSal))
