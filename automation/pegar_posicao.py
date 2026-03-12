# Pegar posição do mouse para usar o comando pyautogui.click
import time
import pyautogui

time.sleep(5)
# Dentro desses 5 segundo, direcione o cursor do mouse no local de captura desejado
print(pyautogui.position())
