#PyAutoGUI lets Python control the mouse and keyboard, and other GUI automation tasks.
#For Windows, macOS, and Linux, on Python 3 and 2.

#importing relevant modules
import pyautogui
import time

#Give the python file some time before continuing
# time.sleep(1) #Can allow the program to give you enough time to move on the screen


# # #Mouse functions
# print(pyautogui.size()) #Prints resolution of screen 
# #Prints the current position of the mouse
# print(pyautogui.position())

# #Moves the mouse over time
# pyautogui.moveTo(x=0,y=0,duration=5)

#Move the mouse relative to its current position
# pyautogui.moveRel(100,100,3)
minimize_x = 1737
minimize_y = 29

# Performing a click on minimize button

# pyautogui.click(x=minimize_x,y=minimize_y,duration=4)

#Other commands
# pyautogui.tripleClick()
# pyautogui.doubleClick()
# pyautogui.leftClick()
# pyautogui.rightClick()

#Scrolling

# #Scrolls down 500
# pyautogui.scroll(-500)
# time.sleep(1)
# #Scrolls up 500
# pyautogui.scroll(500)

# for i in range(10):
#     time.sleep(1)
#     pyautogui.scroll(-300)

#Check if the given coordinates is on screen
# print(pyautogui.onScreen(-1,-1)) # False
# print(pyautogui.onScreen(50,50)) # True