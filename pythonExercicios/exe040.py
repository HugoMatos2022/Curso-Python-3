n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

print('Tirando {} e {} a média do aluno é de: {:.1f} '.format(n1, n2, media))

if media >= 5 and media < 7 :
    print('Aluno está de Recuperação')
elif media < 5 :
    print('Aluno está de Reprovado')
else:
    print('Aluno está Aprovado')
