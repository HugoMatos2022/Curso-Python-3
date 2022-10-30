
import pyautogui

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range (1, 5):
    print('------{}º------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sex = str(input('SEXO F/M: ' )).strip()
    somaidade += idade

    if p == 1 and sex in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sex in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sex in 'Ff' and idade < 20:
            totmulher20 += 1
mediaidade = somaidade /4

print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mis velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo sao {} mulheres com menor de 20 anos'.format(totmulher20))




