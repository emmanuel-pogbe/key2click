import tkinter as tk

root = tk.Tk()
root.title("Calculator app") #Changing title

entry1 = tk.Entry(root,width=35,borderwidth=5)
entry1.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def btadd(number):
    entry1.insert(tk.END,number)
def clear():
    entry1.delete(0,tk.END)
#Define buttons
but1 = tk.Button(root,text="1",padx=40,pady=20,command=lambda: btadd(1))
but2 = tk.Button(root,text="2",padx=40,pady=20,command=lambda: btadd(2))
but3 = tk.Button(root,text="3",padx=40,pady=20,command=lambda: btadd(3))
but4 = tk.Button(root,text="4",padx=40,pady=20,command=lambda: btadd(4))
but5 = tk.Button(root,text="5",padx=40,pady=20,command=lambda: btadd(5))
but6 = tk.Button(root,text="6",padx=40,pady=20,command=lambda: btadd(6))
but7 = tk.Button(root,text="7",padx=40,pady=20,command=lambda: btadd(7))
but8 = tk.Button(root,text="8",padx=40,pady=20,command=lambda: btadd(8))
but9 = tk.Button(root,text="9",padx=40,pady=20,command=lambda: btadd(9))
but0 = tk.Button(root,text="0",padx=40,pady=20,command=lambda: btadd(0))
but_add = tk.Button(root,text="+",padx=39,pady=20,command=lambda: btadd())
but_equal = tk.Button(root,text="=",padx=91,pady=20,command=lambda: btadd())
but_clear = tk.Button(root,text="Clear",padx=79,pady=20,command=clear)


#Put the buttons on the screen
but1.grid(row=3,column=0)
but2.grid(row=3,column=1)
but3.grid(row=3,column=2)

but4.grid(row=2,column=0)
but5.grid(row=2,column=1)
but6.grid(row=2,column=2)

but7.grid(row=1,column=0)
but8.grid(row=1,column=1)
but9.grid(row=1,column=2)

but0.grid(row=4,column=0)
but_add.grid(row=5,column=0)
but_clear.grid(row=4,column=1,columnspan=2)
but_equal.grid(row=5,column=1,columnspan=2)
root.mainloop()