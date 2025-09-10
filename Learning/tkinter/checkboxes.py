import tkinter as tk

class myGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Checkboxes")

        self.var = tk.StringVar()
        #Default on and off values are 1 and 0 (integers)
        self.c = tk.Checkbutton(self.root,text="Male!",variable=self.var,onvalue="On",offvalue="Off") #Why does this alone make the checkbox selected (changing on and off values)
        self.c.deselect() #This is a workaround to the "glitch"
        self.c.pack()

        self.btn1 = tk.Button(self.root,text="Submit",command=self.show).pack()
        self.myLabel = tk.Label(self.root,text=self.var.get())
        self.myLabel.pack()
        tk.mainloop()
    def show(self):
        self.myLabel.config(text=self.var.get())

start = myGui()