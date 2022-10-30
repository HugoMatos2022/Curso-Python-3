nome = str(input('Digite seu nome completo ')).strip()
n = nome.split()
print('Muito prazer em te conhecer {}'.format(nome))
print('Seu último nome é {}'.format(n[len(n)-1]))
print('Seu primeiro nome é {}'. format(n[0]))


