#subpackages - keyboard,mouse
#pynput.mouse contains classes for controlling and monitoring the mouse
#Controlling mouse
from pynput.mouse import Controller,Button,Listener
mouse = Controller()
# mouse.click(Button.left,1) #Clicking left button once on current position


print(f"The current position of mouse is {mouse.position}") #Prints the current position of the mouse

# mouse.move(50,50) #Move mouse (x,y) away from current position
# mouse.scroll(0,-1) #Scroll (x,y) steps; currently set to scroll down 1 step

#Monitoring the mouse
#Use pynput.mouse.Listener like this:

# from pynput.mouse import Listener
# def on_move(x, y):
#     print('Pointer moved to {0}'.format(
#         (x, y)))
# def on_click(x, y, button, pressed):
#     print('{0} at {1}'.format(
#         'Pressed' if pressed else 'Released',
#         (x, y)))
#     if not pressed:
#         # Stop listener
#         return False
# def on_scroll(x, y, dx, dy):
#     print('Scrolled {0} at {1}'.format(
#         'down' if dy < 0 else 'up',
#         (x, y)))
# # Collect events until released
# with Listener(
#         on_move=on_move,
#         on_click=on_click,
#         on_scroll=on_scroll) as listener:
#     listener.join()
# ...or, in a non-blocking fashion:
# listener = Listener(
#     on_move=on_move,
#     on_click=on_click,
#     on_scroll=on_scroll)
# listener.start()