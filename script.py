import pyautogui
import time
import pandas


pyautogui.PAUSE = 0.5
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(x=571, y=393)
pyautogui.write('teste@google.com')
pyautogui.press('tab')
pyautogui.write('1234')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(1)

tabela = pandas.read_csv('produtos.csv')

for linha in tabela.index:

    pyautogui.click(x=611, y=288)

    codigo = tabela.loc[linha, 'codigo']
    marca = tabela.loc[linha, 'marca']
    tipo = tabela.loc[linha, 'tipo']
    categoria = tabela.loc[linha, 'categoria']
    preco_unitario = tabela.loc[linha, 'preco_unitario']
    custo = tabela.loc[linha, 'custo']
    obs = tabela.loc[linha, 'obs']
    
    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    pyautogui.write(str(marca))
    pyautogui.press('tab')
    pyautogui.write(str(tipo))
    pyautogui.press('tab')
    pyautogui.write(str(categoria))
    pyautogui.press('tab')
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')
    pyautogui.write(str(custo))
    pyautogui.press('tab')
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(600)