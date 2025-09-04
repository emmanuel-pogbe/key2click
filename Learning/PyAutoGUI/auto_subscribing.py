import pyautogui
import time
import datetime
'''
1. Open a new tab on the browser
2. Search YouTube.com
3. Search for the channel you want to subscribe
4. Click on the subscribe button
'''
#Ask for prompt
channel_name = pyautogui.prompt(text="",title="Enter channel name")
# Step 1 - open new tab
pyautogui.hotkey("ctrl","t")

#Step 2 - search youtube
pyautogui.write("https://www.youtube.com")
pyautogui.press("enter")
time.sleep(10)

#functions
def click_screen(img):
    try:
        y = pyautogui.locateCenterOnScreen(f"./Learning/PyAutoGUI/images/{img}")
        pyautogui.leftClick(y)
        return True
    except pyautogui.ImageNotFoundException:
        print("Error")
        return False
def find_subscribe(img):
    for i in range(5): #Continues till we find the subscribe button on screen
        try:
            y = pyautogui.locateCenterOnScreen(f"./Learning/PyAutoGUI/images/{img}")
            pyautogui.leftClick(y)
            return True
        except:
            pyautogui.moveTo(tuple(x/2 for x in pyautogui.size())) #Move mouse to center of screen to start scrolling
            time.sleep(0.2)
            pyautogui.scroll(-700) #Scrolls down 
    return False
#Step 3 - search for the channel you want to subscribe and call subscribe function
if click_screen("youtube_search.png") == True:
    time.sleep(0.2)
    pyautogui.write(channel_name,interval=.2)
    pyautogui.press("enter")
    time.sleep(5)
    if find_subscribe("subscribe.png") == True: #Step 4 - Click on the subscribe button
        print(f"Successfully subscribed to {channel_name} at {datetime.datetime.now()}")
    else:
        print("Failed")
else:
    print("Not found")