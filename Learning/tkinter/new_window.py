#Working with other windows

import tkinter as tk
from PIL import ImageTk,Image

class myGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("New windows")
        self.root.iconbitmap("./Learning/tkinter/images/click icon.ico")
        self.btn = tk.Button(self.root,text="Open second window",command=self.open_smth).pack()


        tk.mainloop()
    def open_smth(self):
        self.top = tk.Toplevel()
        self.top.title("Top window")
        self.lbl = tk.Label(self.top,text="Hello World").pack()
        self.my_img = ImageTk.PhotoImage(Image.open("./Learning/tkinter/images/image1.png").resize((200,200)))
        tk.Label(self.top,image=self.my_img).pack()

        self.btn2 = tk.Button(self.top,text="Close window",command=self.top.destroy).pack()


start = myGui()