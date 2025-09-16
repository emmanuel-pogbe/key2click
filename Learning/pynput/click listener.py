from pynput.mouse import Listener
import pyautogui

IS_SELECTED = False
def_position = tuple(x//2 for x in pyautogui.size())
def on_click(x,y,button,pressed):
    # global IS_SELECTED
    global def_position
    # if IS_SELECTED == True:
    #     return False
    def_position = x,y
    return False
def get_a_point():
    print("Click (left or right button) a spot you want to set a shortcut for")
    with Listener(on_click=on_click) as listener:
        listener.join()
    print(f"Position selected: {def_position}")
get_a_point()