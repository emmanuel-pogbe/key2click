from pynput.keyboard import GlobalHotKeys
from pynput.mouse import Listener
import time
import pyautogui
import sys
maps = [] #Points
shorts = ["f","d","g","t","e"] #Shortcuts that can be set Ctrl + ...
def stop_script():
    print("Stopping script...")
    hotkeys.stop()
    sys.exit()
def click_point(index):
    coordinate_x,coordinate_y = maps[index] 
    pyautogui.moveTo(coordinate_x,coordinate_y)
    pyautogui.leftClick()
def set_default():
    return tuple(x//2 for x in pyautogui.size())
def_position = set_default()
def on_click(x,y,button,pressed):
    global def_position
    def_position = x,y
    return False
def add_map_point():
    print("Click (left or right button) a spot you want to set a shortcut for")
    with Listener(on_click=on_click) as l:
        l.join()
    # print(f"Position selected: {def_position}")
    coordinate_x,coordinate_y = def_position
    maps.append((coordinate_x,coordinate_y))
    print(f"Coordinates -> {coordinate_x},{coordinate_y}")
    print(f"Shortcut set to ctrl + {shorts[len(maps)-1]}")
while len(maps)<6:
    print(f"You can add up to 5 points for shortcuts, {len(maps)} shortcuts selected")
    proceed = input("Press any key to continue")
    add_map_point()
    proceed = input("Add another point for a shortcut (y/n)").lower()
    if proceed != 'y':
        break
hotkey_map = {
    f"<ctrl>+{shorts[i]}": (lambda idx=i: click_point(idx)) for i in range(len(maps))
}
hotkey_map["<shift>+<esc>"] = stop_script
print("Press 'shift + esc' to quit")
hotkeys = GlobalHotKeys(hotkey_map)
hotkeys.start()
hotkeys.join()
print("Thanks for being here!")