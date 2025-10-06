import tkinter as tk
from tkinter import filedialog
import json
x = {1:2,3:4,5:6}
def open_dialog():
    file1 = filedialog.asksaveasfile("w",defaultextension="json",filetypes=[("JSON files", "*.json")],title="Export loaded shortcuts")
    json.dump(x,file1,indent=2)
    file1.close

app = tk.Tk()
but = tk.Button(master=app,text="Save to file",command=open_dialog)
but.pack()
app.mainloop()
