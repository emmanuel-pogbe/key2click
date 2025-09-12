import tkinter as tk

class myGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DropDown!")
        self.root.geometry("400x400")

        #Drop down boxes
        self.clicked = tk.StringVar()
        self.clicked.set("Monday")
        #Passing all options directly in class
        self.drop = tk.OptionMenu(self.root,self.clicked,"Monday","Tuesday","Wednesday","Thursday","Friday")
        #Using a list to get dropdowns
        options = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
        ]
        self.clicked.set(options[0])
        self.drop = tk.OptionMenu(self.root,self.clicked,*options) #Notice the star before the variable 'option'
        self.drop.pack()

        self.myButton = tk.Button(self.root,text="Show Selection",command=self.show)
        self.myButton.pack()
        tk.mainloop()

    def show(self):
        x = tk.Label(self.root,text=self.clicked.get())
        x.pack()
start = myGui()