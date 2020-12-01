import time
import os
import pyautogui


def countdown(arg):
    for i in range(0, arg):
        print("\r", end='')
        print("%i" % int(arg - i), end='', flush=True)
        time.sleep(1)


os.startfile('notepad.exe')

try:
    while True:
        pyautogui.moveTo(959.5, 539.5)
        pyautogui.click(button='left')
        pyautogui.write('NICK BIG GAY ')

except KeyboardInterrupt:
    print('s')

