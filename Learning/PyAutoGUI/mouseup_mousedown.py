#Working with mouseup and mousedown to draw a triangle in paint

import pyautogui
import time
x = 212
y = 293
def draw_triangle(x,y): #Draws a triangle in paint
    pyautogui.moveTo(x,y,duration=2)
    pyautogui.mouseDown(x,y)
    pyautogui.moveRel(-100,100,duration=1)
    pyautogui.moveRel(200,0,duration=1)
    pyautogui.moveRel(-100,-100,duration=1)
    pyautogui.mouseUp()
def draw_box(x,y): #Draws a box
    pyautogui.moveTo(x,y,duration=2)
    pyautogui.mouseDown(x,y)
    pyautogui.moveRel(0,500,duration=3)
    pyautogui.moveRel(500,0,duration=3)
    pyautogui.moveRel(0,-500,duration=3)
    pyautogui.moveRel(-500,0,duration=3)
    pyautogui.mouseUp()
def draw_bottom_corner(x,y,distance):
    c = distance
    pyautogui.mouseDown(x,y)
    pyautogui.moveRel(-c,0,duration=0)
    pyautogui.moveRel(0,-c,duration=0)
    pyautogui.mouseUp()
