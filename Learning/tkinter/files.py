import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

class myGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Working with files")
        self.btn = tk.Button(self.root,text="Open file",command=self.open_file).pack()
        tk.mainloop()
    def open_file(self):
        #askopenfilename() returns the path of the file selected which can then be used to open the file
        self.filename = filedialog.askopenfilename(title="Select a file",filetypes=(("png files","*.png"),("jpeg files","*.jp*g")))
        
        self.myLabel = tk.Label(self.root,text=self.filename).pack()
        try:
            self.img = ImageTk.PhotoImage(Image.open(self.filename).resize((100,100)))
            self.img_label = tk.Label(self.root,image=self.img).pack()
        except FileNotFoundError:
            tk.Label(self.root,text="No image selected").pack()
start = myGui()
