import tkinter as tk

root = tk.Tk()
root.geometry("200x200")

def myClick():
    myLabel = tk.Label(root,text="You clicked me")
    myLabel.pack()
#Using the command parameter to make a button do something -> Notice you don't pass the function name with a parameter
myButton = tk.Button(root,text="Click me!",padx=50,pady=50,command=myClick,bg="#ffffff")
myButton.pack()

root.mainloop()