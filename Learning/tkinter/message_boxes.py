import tkinter as tk
from tkinter import messagebox

#Message box types:
#showinfo, showwarning, showerror
#askquestion,askokcancel,askyesno
class myGui:
    def __init__(self):
        self.root = tk.Tk()
        self.button = tk.Button(self.root,text="Popup",command=self.popup)
        self.button.pack()
        tk.mainloop()
    def popup(self):
        response = messagebox.showinfo("Popup","Hello World")
        tk.Label(self.root,text=response).pack()
start = myGui()