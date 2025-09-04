import pyautogui
import time
time.sleep(1)
def decrement(d):
    return d-30
def draw_spiral():
    distance = 700
    while distance>0:
        pyautogui.dragRel(xOffset=distance,yOffset=0,duration=1)
        distance = decrement(distance)
        pyautogui.dragRel(xOffset=0,yOffset=distance,duration=1)
        pyautogui.dragRel(xOffset=-distance,yOffset=0,duration=1)
        distance = decrement(distance)
        pyautogui.dragRel(xOffset=0,yOffset=-distance,duration=1)
        time.sleep(1)
