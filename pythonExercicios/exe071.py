print('#'*20)
print('{:^20}'.format('Banco Fala que te Empresto'))
print('#'*20)

valor = int(input('Que valor voce quer sacar? R$'))
total = valor
céd = 50
totcéd = 0

while True:
    if total >= céd:
        total -= céd
        totcéd +=1

    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0

        if total == 0:
            break
