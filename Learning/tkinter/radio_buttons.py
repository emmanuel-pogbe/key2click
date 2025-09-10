import tkinter as tk

class myGui:
    def __init__(self):
        self.root = tk.Tk()
        # self.r = tk.IntVar()
        # self.r.set(1) #Setting default selection
        # self.radio1 = tk.Radiobutton(self.root,text="Option 1",variable=self.r,value=1,command=self.clicked)
        # self.radio1.pack()
        # self.radio2 = tk    .Radiobutton(self.root,text="Option 2",variable=self.r,value=2,command=self.clicked)
        # self.radio2.pack()


        #Pizza toppings
        MODES = [
            ("Pepper","Pepper"),
            ("Cheese","Cheese"),
            ("Mushroom","Mushroom"),
            ("Onion","Onion"),
        ]
        self.topping = tk.StringVar()
        self.topping.set("Pepper")
        for top,val in MODES:
            self.tempRad = tk.Radiobutton(self.root,text=top,variable=self.topping,value=val,command=self.clicked)
            self.tempRad.pack()
        self.myLabel = tk.Label(self.root,text=self.topping.get())
        self.myLabel.pack()
        tk.mainloop()
    def clicked(self):
        self.myLabel.config(text=self.topping.get())

start = myGui()