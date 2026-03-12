import pyautogui
import pandas
import time # controle de tempo

pyautogui.PAUSE = 0.5 # por padrão, não há pausa, colocando "1", haverá pausa de 1 segundo 
#entre os comandos

# definindo "link" como a URL do site que usaremos para facilitar o uso
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# Passo a passo do projeto

# Passo 1: Entrar no sistema da empresa

    # abrir navegador
pyautogui.press("win") # pressionando a tecla windows
pyautogui.write("brave") # selecionando o navegador
#pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)

    # acessando o site
pyautogui.write(link)
pyautogui.press("enter")
# fazer uma pausa maior para o site carregar sem problemas
time.sleep(3) # em segundos

# Passo 2: Fazer login no site

    # clicar no campo de email -> executar "pegar_posicao.py"
pyautogui.click(x=505, y=366) # posição medida individuamente (o valor muda dependendo da máquina)
pyautogui.write("abcd@gmail.com") # email
pyautogui.press("tab")
pyautogui.write("1234") # senha
pyautogui.press("tab")
pyautogui.press("enter")
# fazer uma pausa maior para o site carregar sem problemas
time.sleep(3)

# Passo 3: Abrir base de dados (importar o arquivo)

    # lendo a base de dados e armazenando em "tabela"
tabela = pandas.read_csv("produtos.csv")

# Passo 4: Cadastrar apenas 1 produto 
"""
pyautogui.click(x=646, y=249) # clicar no campo "Código do Produto"
pyautogui.write("MOLO00251")
pyautogui.press("tab")

    #Campo atual: "Marca do Produto"
pyautogui.write("Nike")
pyautogui.press("tab")

    #Campo atual: "Tipo do Produto"
pyautogui.write("Tênis")
pyautogui.press("tab")

    #Campo atual: "Categoria do Produto"
pyautogui.write("categoria")
pyautogui.press("tab")

    #Campo atual: "Preço Unitário do Produto"
pyautogui.write("preço")
pyautogui.press("tab")

#Campo atual: "Custo do Produto"
pyautogui.write("custo")
pyautogui.press("tab")

#Campo atual: "OBS"
pyautogui.write("obs")
pyautogui.press("tab")

pyautogui.press("enter") # campos preenchidos
"""

# Passo 5: Repetir o passo 4 até acabar a lista de produtos, 
# ou seja, cadastras x produtos

for linha in tabela.index:
    pyautogui.click(x=646, y=249) # clicar no campo "Código do Produto"
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

        #Campo atual: "Marca do Produto"
    marca =str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

        #Campo atual: "Tipo do Produto"
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

        #Campo atual: "Categoria do Produto"
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

        #Campo atual: "Preço Unitário do Produto"
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    #Campo atual: "Custo do Produto"
    custo = str(tabela.loc[linha, "custo" ])
    pyautogui.write(custo)
    pyautogui.press("tab")

    #Campo atual: "OBS"
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter") # campos preenchidos

    pyautogui.scroll(5000) # retornando ao início da tela para preencher
    # um novo produto