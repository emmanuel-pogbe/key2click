import tkinter as tk
from PIL import Image, ImageTk

class MyGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Working with frames")
        self.root.iconbitmap("./Learning/tkinter/images/click icon.ico")
        self.frame = tk.LabelFrame(self.root,border=0,padx=50,pady=50) #Padding inside frame
        self.frame.pack(padx=100,pady=100) #Padding outside frame

        self.b = tk.Button(self.frame,text="Click me!") #Putting stuff inside frames
        self.b.pack()

        self.root.mainloop()

start = MyGui()