import tkinter as tk

root = tk.Tk() 
#Creating a label widget
myLabel = tk.Label(root,text="Hello World")
#Shoving it onto the screen
myLabel.pack()

root.mainloop()
