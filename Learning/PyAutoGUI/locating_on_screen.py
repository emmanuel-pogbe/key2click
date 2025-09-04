import pyautogui
import time
#There is a confidence attribute in locateOnScreen() function family
#takes a floating point number between 0 and 1
#It basically says even if there is an X*100% match on the iamge then accept that
#It requires the opencv module - 'pip install opencv-python'
def get_search_position():
    try:
        y = pyautogui.locateCenterOnScreen("./Learning/PyAutoGUI/images/reference.png")
    except pyautogui.ImageNotFoundException:
        try:
            y = pyautogui.locateCenterOnScreen("./Learning/PyAutoGUI/images/search.png")
        except:
            size = pyautogui.size()
            y = size[0]/2,size[1]/2
    return y
pyautogui.moveTo(get_search_position())
time.sleep(0.1)
pyautogui.leftClick()
