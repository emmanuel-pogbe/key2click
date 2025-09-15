from pynput.keyboard import GlobalHotKeys
import time
import pyautogui
def search():
    pyautogui.moveTo(coordinate_x,coordinate_y)
    pyautogui.leftClick()
print("Move your mouse to the point you want to set a shortcut for")
print("You have 5 seconds")
time.sleep(5)
coordinate_x,coordinate_y = pyautogui.position()
print(f"Coordinates -> {coordinate_x},{coordinate_y}")
print("Press ctrl + f to activate")
hotkeys = GlobalHotKeys({
    "<ctrl>+f":search
})
hotkeys.start()
hotkeys.wait()
input()
hotkeys.stop()
