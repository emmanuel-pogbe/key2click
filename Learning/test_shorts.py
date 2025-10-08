from pynput.keyboard import GlobalHotKeys
from pynput.keyboard import HotKey
HotKey.parse
def is_valid_shortcut(s: str):
    try:
        x = HotKey.parse(s)
        return x
    except ValueError:
        return False
print(is_valid_shortcut("<>"))