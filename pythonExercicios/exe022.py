nome = str(input('Digite o seu nome completo:')).strip() # com esse metodo strip() ele já elimina os espaços em brancos digitados pelos usuários
print('Nome todo em maiusculo :{}' .format(nome.upper()))
print('Nome todo em minusculo :{}' .format(nome.lower()))
print('Seu nome ao todo tem {} letras.' .format(len(nome) - nome.count(' '))) # metodo -count(' ') nao coloca na contagem os espaços digitados pelos ususarios
#print('Seu primeiro nome tem {} letras' .format(nome.find(' ')))
separa = nome.split() # Divide a cadeia de caractere em palavras até sofrerem os espaços
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
