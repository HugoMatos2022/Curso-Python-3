sal = float(input('Qual o salário do funcionário? R$'))
novoSal = sal + (sal * 15 / 100)
print('O funcionário que ganhava R${} com o aumento de 15% passa a receber R${:0.2f}'.format(sal, novoSal))
