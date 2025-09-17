from pynput import keyboard
from pynput.keyboard import GlobalHotKeys
import sys
def hmm():
    c = keyboard.Controller()
    c.type("Hii")
with GlobalHotKeys({"<f2>":hmm,"<esc>":sys.exit}) as g:
    g.join()
