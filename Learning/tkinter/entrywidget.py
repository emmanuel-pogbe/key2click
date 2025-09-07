import tkinter as tk
root = tk.Tk()
root.geometry("200x200")
entry1 = tk.Entry(root,width=20) #Creating a simple entry
#Purpose: Designed for single-line text input.
#Use Case: Ideal for things like usernames, passwords, or short responses.

# entry1.get() #Function gets whatever is inputted
entry1.pack()
# entry1.insert(0,"Enter Your Name:") #Creating default text

def getText():
    label1 = tk.Label(root,text=entry1.get())
    label1.pack()
button1 = tk.Button(root,padx=10,pady=10,text="Click me!",command=getText)
button1.pack()



root.mainloop()