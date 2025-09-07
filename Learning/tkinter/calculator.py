import tkinter as tk

root = tk.Tk()
root.title("Calculator app") #Changing title

entry1 = tk.Entry(root,width=35,borderwidth=5)
entry1.grid(row=0,column=0,columnspan=3,padx=10,pady=10)


root.mainloop()