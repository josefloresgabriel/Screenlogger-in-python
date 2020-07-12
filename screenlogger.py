import pyautogui
from time import sleep
from datetime import *

while True:
    sleep(5)
    im1 = pyautogui.screenshot()
    im1.save(f'{datetime.now()}.png')
