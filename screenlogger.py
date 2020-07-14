import pyautogui
from pynput.mouse import Button, Listener
from datetime import *

def clicou(x,y, botao, pressionado):
    if pressionado == True:
        im1 = pyautogui.screenshot()
        im1.save(f'{datetime.now()}.png')

listener = Listener(on_click=clicou)
listener.start()
listener.join()