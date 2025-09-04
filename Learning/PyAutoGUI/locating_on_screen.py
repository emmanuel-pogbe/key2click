import pyautogui
import time

def get_search_position():
    try:
        y = pyautogui.locateCenterOnScreen("./Learning/PyAutoGUI/images/reference.png")
    except pyautogui.ImageNotFoundException:
        try:
            y = pyautogui.locateCenterOnScreen("./Learning/PyAutoGUI/images/search.png")
        except:
            size = pyautogui.size()
            y = size[0]/2,size[1]/2
    return y
pyautogui.moveTo(get_search_position())
time.sleep(0.1)
pyautogui.leftClick()
