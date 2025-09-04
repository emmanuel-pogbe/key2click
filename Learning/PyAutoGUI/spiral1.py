import pyautogui
def draw_top_corner(x,y,distance):
    c = distance
    pyautogui.mouseDown(x,y)
    pyautogui.moveRel(c,0,duration=0)
    pyautogui.moveRel(0,c,duration=0)
    pyautogui.mouseUp()
def draw_spiral(x,y,starting_distance):
    dist = starting_distance
    new_x,new_y= x,y
    for i in range(8):
        dist -=30
        draw_top_corner(new_x,new_y,dist)
        dist -= 30
        new_x, new_y = pyautogui.position()
        draw_bottom_corner(new_x,new_y,dist)
        new_x,new_y = pyautogui.position()
draw_spiral(x,y,500)