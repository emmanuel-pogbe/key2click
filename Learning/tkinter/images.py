import tkinter as tk
from PIL import ImageTk, Image  #

root = tk.Tk()
root.title("Start")
#Setting an icon - has to be an ico file
root.iconbitmap("./Learning/tkinter/images/click icon.ico")
#Working with images
#By default, the PhotoImage class in Tkinter only supports:
    #GIF
    #PGM/PPM (Portable Graymap/Portable Pixmap)
#To break free from this limitation, 
#most Python developers use the Pillow library (a modern fork of PIL)

img = Image.open("./Learning/tkinter/images/keyboard.jpg") #1. Open image and process image
#Resizing images so it fits widgets
resized_img = img.resize((200,200))
my_img = ImageTk.PhotoImage(resized_img) 

my_label = tk.Label(root,image=my_img) #2. Place image in a widget
my_label.pack() #3. Put it on the screen


#Creating an exit button
button_quit = tk.Button(root,text="Exit program",command=root.quit)
button_quit.pack()
root.mainloop()