from pynput.keyboard import Controller,HotKey,Key
import time

#Controlling the keyboard
keyboard = Controller()

#     Select all
# with keyboard.pressed(Key.ctrl):
#     keyboard.press("a")
#     keyboard.release("a")

#Open word web
with keyboard.pressed(Key.ctrl):
    with keyboard.pressed(Key.alt):
        keyboard.press('w')
        keyboard.release('w')
time.sleep(2)
#Search for word on wordweb using type method
keyboard.type("Oxygen")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
