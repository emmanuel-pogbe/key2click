import tkinter as tk

class myGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Working with sliders")
        #Vertical slider
        self.vertical = tk.Scale(self.root,from_=0,to=100)
        self.vertical.pack()

        #Horizontal slider
        self.horizontal = tk.Scale(self.root,from_=0,to=100,orient="horizontal",command=self.update_slider2)
        self.horizontal.pack()

        self.my_label = tk.Label(self.root,text=self.horizontal.get())
        self.my_label.pack()
        #Using button to update
        self.update = tk.Button(self.root,text="Update slider!",command=self.update_slider)
        self.update.pack()
        tk.mainloop()
    def update_slider(self):
        self.my_label.config(text=self.horizontal.get())
    def update_slider2(self,var): #For some reason, you have to pass a second filler argument, don't know why yet
        self.my_label.config(text=self.horizontal.get())
start = myGui()