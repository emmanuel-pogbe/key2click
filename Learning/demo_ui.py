import tkinter as tk
import tkinter.ttk
class myGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Key2Click")
        self.root.attributes("-topmost",True)
        # self.root.overrideredirect(True)
        self.root.attributes("-alpha",0.3) #Semi-transparent
        self.root.geometry("500x500")
        self.root.iconbitmap("./Learning/click icon.ico")
        self.main_label = tk.Label(master=self.root,text="Key2Click",font="Calibri 20 bold")
        self.main_label.pack()
        # self.root.config(cursor="crosshair") #Can be useful later
        self.root.mainloop()
start = myGui()
