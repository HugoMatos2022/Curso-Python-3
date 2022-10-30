vel = float(input('Qual a velocidade do carro? '))
if vel > 80:
    print('MULTADO, voce excedeu o limite permitido de 80km/h')
    multa = (vel - 80) * 7 # calcula o valor da multa a ser paga, considerando apenas o km acima do permitido
    print('Voce deve pagar uma multa de R${:.2f}'.format(multa))
print('TENHA UM BOM DIA E DIRIJA COM SEGURANÇA')