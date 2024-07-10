# pip install pyautogui
# pip install pandas openpyxl numpy

# Passo 1 - Entrar no sistema da empresa
#   link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2 - Fazer login
# Passo 3 - Pegar/Importar a base de dados
# Passo 4 - Cadastrar o produto
# Passo 5 - Repetir o passo 4 até cadastrar todos os produtos

import pyautogui
import time

# pyautogui.click - clicar com o mouse
# pyautogui.write - escrever texto
# pyautogui.press - apertar 1 tecla
# pyautogui.hotkey - combinação de telcas (ctrl C)
# pyautogui.scroll - rolar a tela para cima ou para baixo

pyautogui.PAUSE = 0.5
## Passo 1 - Entrar no sistema da empresa
# Abrir no navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(3)

## Passo 2 - Fazer login
pyautogui.click(x=-870, y=405)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write('python@gmail.com')

# passar para o campo de senha
pyautogui.press('tab')
pyautogui.write('123')
pyautogui.click(x=-807, y=564)

time.sleep(3)

## Passo 3 - Pegar/Importar a base de dados
import pandas

tabela = pandas.read_csv('produtos.csv')

## Passo 4 - Cadastrar o produto
# para cada linha da tabela: 
for linha in tabela.index:
    # codigo
    pyautogui.click(x=-971, y=292)
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)

    #marca
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')
    pyautogui.write(marca)

    # tipo
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')
    pyautogui.write(tipo)

    # categoria
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.press('tab')
    pyautogui.write(categoria)

    # preco_unitario
    preco = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.press('tab')
    pyautogui.write(preco)

    # custo
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.press('tab')
    pyautogui.write(custo)

    # obs
    obs = str(tabela.loc[linha, 'obs'])
    pyautogui.press('tab')
    if obs != 'nan':
        pyautogui.write(obs)

    # botao de enviar
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.press('pageup')

## Passo 5 - Repetir o passo 4 até cadastrar todos os produtos - para todas as linhas da tabela