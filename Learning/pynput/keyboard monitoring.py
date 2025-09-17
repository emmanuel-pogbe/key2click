from pynput.keyboard import Listener,Key
import time

def on_press(key):
    try:
        char = key.char
        print(char)
    except:
        print(key)
def on_release(key):
    if key == Key.esc:
        #Stop listener
        return False
    try:
        char = key.char
        print(char)
    except:
        print(key)
with Listener(on_press=on_press,on_release=on_release) as l:
    l.join()

