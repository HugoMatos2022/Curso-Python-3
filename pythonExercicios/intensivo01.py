import pyautogui
import time
import pyperclip
import pandas


#passo 1 : entrar no sistema (no caso vai ser entrar no link)
pyautogui.press('winleft') # pressiona uma atalho do teclado por meio de uma tecla
time.sleep(2) # espera um segundo pra seguir
pyautogui.write('chrome') # escreve o programa que eu quero
pyautogui.press('enter') # aperta enter pra abrir o navegador
time.sleep(5) # espera um segundo pra ir ao proximo passp
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga') # copia o endereço desejado
pyautogui.hotkey('ctrl','v') # Cola o endereço no campo de busca do navegador
pyautogui.press('enter') # Aperta enter para seguir pro endereço digitado
time.sleep(5)

# passo 2 : Navegar no sistema e encontrar a base de dados(entrar na pasta Exportar)
pyautogui.click(x=364, y=269, clicks=2) # Valores de X e Y representam a dimensao da tela em que esta a 'caixinha ' a ser clicada
time.sleep(5)

# passo 3 : Download da base de dados
pyautogui.click(x=347, y=332, clicks=1) # clicou no arquivo
time.sleep(2)
pyautogui.click(x=1164, y=164, clicks=1) # clicou nos tres pontinhos
time.sleep(2)
#pyautogui.click(x=938, y=566) # Fez o download
import openpyxl

# passo 4 : Calcular os indicadores(faturamento, quantidade de produtos )
import pyperclip

tabela = pandas.read_excel(r'C:\Users\hugo\Downloads\Vendas - Dez.xlsx') # Localiza o nome do arquivo e o local e tras ao código
print(tabela)
quantidade = tabela['Quantidade'].sum() # Soma da coluna quantidade
faturamento = tabela['Valor Final'].sum()  # Soma da coluna valor final
print('A quantidade total de produtos vendido foi de: {}'.format(quantidade))
print('O valor total de faturamento foi de R$:{}'.format(faturamento))

# passo 5 : Entrar no email
pyautogui.hotkey('ctrl', 't') # abre uma nova aba
time.sleep(1)
pyperclip.copy('https://outlook.live.com/mail/0/') # Copiar link do email
pyautogui.hotkey('ctrl', 'v') # abrir link do email
time.sleep(5)
pyautogui.press('enter') # entrar no email
time.sleep(9)
# passo 6 : Mandar o email
pyautogui.click(x=186, y=122, clicks=1) # Clica no botao para escrever um novo email
time.sleep(2)
pyautogui.write('hugo.oliveiradematos@hotmail.com') # Digita o email
pyautogui.press('tab') # seleciona o email
#pyautogui.press('tab') # passar pro proximo campo
pyautogui.write('Relatório de Vendas ')
pyautogui.press('tab')
texto = f"""
Prazados, Boa tarde

O faturamento de ontem foi de R$ {faturamento:,.2f}
A quantidade de produtos vendidos foi de: {quantidade:,}"""

pyautogui.write(texto)
pyautogui.hotkey('ctrl','enter')



