from pynput.mouse import Button,Listener,Controller
import pyautogui
import time

IS_SELECTED = False
def_position = tuple(x//2 for x in pyautogui.size())
def on_click(x,y,button,pressed):
    global IS_SELECTED
    global def_position
    if IS_SELECTED == True:
        return False
    def_position = x,y
    IS_SELECTED = True
print("Click a spot you want to set a shortcut for")
with Listener(on_click=on_click) as listener:
    listener.join()
print(f"Position selected: {def_position}")