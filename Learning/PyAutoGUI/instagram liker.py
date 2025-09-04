import pyautogui
import time
#This only works on instagram on Google chrome browser on certain conditions
#Zoom - 90%
time.sleep(2)
print(pyautogui.position())
post_x = 530
post_y = 556
like_x = 1057
like_y = 793
like_reel_x = 877
like_reel_y = 796
next_x = 1867
next_y = 562
next_reel_x = 1866
next_reel_y = 558
def like_reel():
    pyautogui.mouseDown(x=like_reel_x,y=like_reel_y)
    time.sleep(0.3)
    pyautogui.mouseUp()
    time.sleep(2)
    pyautogui.click(next_reel_x,next_reel_y,duration=1) 
for i in range(3):
    time.sleep(2)
    like_reel()