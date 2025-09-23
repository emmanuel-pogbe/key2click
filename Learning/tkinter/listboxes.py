import tkinter as tk
class myGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Listboxes testing")
        self.root.geometry("400x800")
        #Create a frame and scrollbar
        self.my_frame = tk.Frame(master=self.root)
        self.scroll = tk.Scrollbar(master=self.my_frame,orient=tk.VERTICAL,width=20)

        #When something is selected in your listbox, it becomes the anchor - tk.ANCHOR
        #Listbox
        #selectmode options:
        #SINGLE, BROWSE, MULTIPLE, EXTENDED
        self.my_listbox = tk.Listbox(master=self.my_frame,width=50,yscrollcommand=self.scroll.set,selectmode=tk.EXTENDED)
        #Configure scrollbar
        self.scroll.config(command=self.my_listbox.yview)
        self.scroll.pack(side=tk.RIGHT,fill=tk.Y)
        self.my_frame.pack()
        self.my_listbox.pack(pady=15)

        #Add item to listbox
        self.my_listbox.insert(tk.END,"This is an item") #Index then string for arguments
        self.my_listbox.insert(tk.END,"Last item") #tk.END puts it at the end
        
        #Add a list of items
        self.my_l = ["One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen"]
        for item in self.my_l:
            self.my_listbox.insert(tk.END,item)
        self.my_button = tk.Button(master=self.root,text="Delete",command=self.delete)
        self.my_button.pack(pady=10)

        self.my_button2 = tk.Button(master=self.root,text="Select",command=self.select)
        self.my_button2.pack(pady=10)
    
        self.my_button3 = tk.Button(master=self.root,text="Delete all",command=self.delete_all)
        self.my_button3.pack(pady=10)

        self.my_button4 = tk.Button(master=self.root,text="Select all",command=self.select_all)
        self.my_button4.pack(pady=10)

        self.my_button5 = tk.Button(master=self.root,text="Delete multiple",command=self.delete_multiple)
        self.my_button5.pack(pady=10)

        self.my_label = tk.Label(master=self.root,text='')
        self.my_label.pack(pady=5)
        tk.mainloop()
    def delete(self): #When something is selected in your listbox, it becomes the anchor - tk.ANCHOR
        self.my_listbox.delete(tk.ANCHOR)
    def select(self):
        self.my_label.config(text=self.my_listbox.get(tk.ANCHOR))
    def delete_all(self):
        self.my_listbox.delete(0,tk.END)
    def select_all(self):
        result = ""
        for item in self.my_listbox.curselection():
            result = result + f"{self.my_listbox.get(item)}\n"
        self.my_label.config(text=result)
    def delete_multiple(self):
        for item in reversed(self.my_listbox.curselection()): #reverse the list so that we can delete from the end so as not to affec the current list
            self.my_listbox.delete(item)
        
start = myGui()