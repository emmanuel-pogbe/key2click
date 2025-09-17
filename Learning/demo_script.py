from pynput.keyboard import GlobalHotKeys
from pynput.mouse import Listener
import time
import pyautogui
import sys
import json
maps = [] #Points
shortcuts = {
    # shortcut : (x,y)
}
def save_shortcuts():
    with open("shortcuts-demo.json","w") as js:
        json.dump(shortcuts,js,indent=2)
def load_shortcuts():
    try:
        with open("shortcuts-demo.json","r") as js:
            all_shortcuts = json.load(js)
        return all_shortcuts
    except FileNotFoundError:
        return "File not found"

def stop_script():
    print("Stopping script...")
    sys.exit()

def click_point(shortcut_key):
    coordinate_x,coordinate_y = shortcuts[shortcut_key] 
    try:
        pyautogui.moveTo(coordinate_x,coordinate_y)
        pyautogui.leftClick()
    except:
        pass

def set_default():
    return tuple(x//2 for x in pyautogui.size())

default_position = set_default()

def on_click(x,y,button,pressed):
    global default_position
    default_position = x,y
    return False

def get_shortcut():
    shortcut = input("Enter shortcut in specific format (e.g ctrl+f, ctrl+shift+l, alt+4): ").lower()
    br = shortcut.split("+")
    for i in range(len(br)):
        br[i] = br[i].strip()
        if len(br[i])>1:
            br[i] = f"<{br[i]}>"
    return "+".join(br)

def add_map_point():
    print("Click (left or right button) a spot you want to set a shortcut for")
    with Listener(on_click=on_click) as l:
        l.join()
    # print(f"Position selected: {default_position}")
    coordinate_x,coordinate_y = default_position
    # maps.append((coordinate_x,coordinate_y))
    print(f"Coordinates -> {coordinate_x},{coordinate_y}")
    while True:
        shortcut = get_shortcut()
        if shortcuts.get(shortcut) == None:
            shortcuts[shortcut] = (coordinate_x,coordinate_y)
            print(f"Shortcut set to {shortcut}")
            break
        else:
            print("Shortcut already exists on another point, pick another one!")
    
while True:
    print(f"Add points for shortcuts, {len(shortcuts)} shortcuts selected")
    proceed = input("Press any key to continue: ")
    add_map_point()
    proceed = input("Add another point for a shortcut (y/n): ").lower()
    if proceed != 'y':
        break
save_shortcuts()
hotkey_map = {
    i : (lambda idx=i: click_point(idx)) for i in shortcuts
}
hotkey_map["<shift>+<esc>"] = stop_script
print("Press 'shift + esc' to quit")
# hotkeys = GlobalHotKeys(hotkey_map)
# hotkeys.start()
# hotkeys.join()
with GlobalHotKeys(hotkey_map) as g:
    g.join()
print("Thanks for being here!")