import tkinter
class myGui:
    def __init__(self):
        self.root = tkinter.Tk()
        # self.root.geometry("1000x200")
        self.label = tkinter.Label(self.root,text="Hello World!")
        self.label2 = tkinter.Label(self.root,text="This is not my first GUI program",font=("Times New Roman",12))
        self.label.pack(side="left")
        self.label2.pack(side="left")
        self.root.mainloop()
mygui = myGui()
