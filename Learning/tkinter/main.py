import tkinter as tk
root = tk.Tk() #Create application

root.geometry("500x500") #Setting size (length * height) 
root.title("Key2Click") #Setting title

label = tk.Label(root,text="Hello World",font=('Arial',18)) #Label
label.pack(pady=20)

textbox = tk.Text(root,height=3,font=('Arial',14)) #Textbox; height specifies how many lines
textbox.pack(padx=10)

# myentry = tk.Entry(root) #Simple text entry, only supports one line
# myentry.pack(pady=10)

# button = tk.Button(root,text="Click me!",font=("Arial",25)) #Basic buttons
# button.pack(pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)

btn1 = tk.Button(buttonframe,text="1")
btn1.grid(row=0,column=0,sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe,text="2")
btn2.grid(row=0,column=1,sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe,text="3")
btn3.grid(row=0,column=2,sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe,text="4")
btn4.grid(row=1,column=0,sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe,text="5")
btn5.grid(row=1,column=1,sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe,text="6")
btn6.grid(row=1,column=2,sticky=tk.W+tk.E)

buttonframe.pack(fill='x') #Stretch along the x axis

anotherbtn = tk.Button(root,text="TEST")
anotherbtn.place(x=200,y=200,height=100,width=100) #Place widget manually, can be placed on other elements

root.mainloop()
