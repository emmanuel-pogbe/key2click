from pynput.mouse import Controller,Button
import time
import pyautogui


mouse = Controller()

prev_position = (836,535)
new_position = (100,100)

def move_icon():
    pyautogui.moveTo(prev_position[0],prev_position[1])
    time.sleep(0.12)
    mouse.press(Button.left)
    time.sleep(0.12)
    pyautogui.moveTo(new_position[0],new_position[1])
    time.sleep(0.12)
    mouse.release(Button.left)

time.sleep(2)
# move_icon()
# print(pyautogui.position())
# mouse.scroll(0,-1) #Scroll down a step  




