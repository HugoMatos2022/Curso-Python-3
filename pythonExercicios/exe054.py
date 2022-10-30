from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for pessoa in range(1, 8):
    nas = int(input('Em que ano {}º pessoa nasceu?'.format(pessoa)))
    idade = atual - nas
    if idade >= 21:
       totmaior += 1
    elif idade < 21:
       totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade' .format(totmenor))

