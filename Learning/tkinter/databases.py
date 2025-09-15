import sqlite3
import tkinter as tk


class myGui:
    def __init__(self,root):
        self.root = root
        self.root.title("Hello World")  
        self.conn = sqlite3.connect("./Learning/test.db")
        self.c = self.conn.cursor()
        self.table = "addresses"
        self.create_table(self.table)
        self.f_name = tk.Entry(self.root,width=30)
        self.f_name.grid(row=0,column=1,padx=20)

        self.l_name = tk.Entry(self.root,width=30)
        self.l_name.grid(row=1,column=1,padx=20)

        self.address = tk.Entry(self.root,width=30)
        self.address.grid(row=2,column=1,padx=20)
        
        self.f_name_label = tk.Label(self.root,text="Enter first name:")
        self.f_name_label.grid(row=0,column=0)
        self.l_name_label = tk.Label(self.root,text="Enter last name:")
        self.l_name_label.grid(row=1,column=0)
        self.address_label = tk.Label(self.root,text="Enter address:")
        self.address_label.grid(row=2,column=0)

        self.submitBtn = tk.Button(self.root,text="Submit",command= lambda: self.submit(self.table))
        self.submitBtn.grid(row=3,column=0,pady=10,ipadx=50)

        self.query = tk.Button(self.root,text="Show all records",command=self.show_all)
        self.query.grid(row=3,column=1,ipadx=50)

        self.submission = tk.LabelFrame(self.root,border=0)
        self.submission.grid(row=4,column=0,columnspan=2)
        self.success_label = tk.Label(self.submission,text="")
        self.success_label.pack()
    def create_table(self,table_name):
        self.c.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
                       first_name text,
                       last_name text,
                       address text)
                       """)
    def submit(self,table_name):
        self.clear()
        first_name = self.f_name.get()
        last_name = self.l_name.get()
        address = self.address.get()
        try:
            self.c.execute(f"INSERT INTO {table_name} VALUES (?,?,?)",(first_name,last_name,address))
            self.success_label.config(text="Success")
        except BaseException as e:
            self.success_label.config(text=f"Error: {e} :(",pady=5)
    def clear(self):
        self.f_name.delete(0,tk.END)
        self.l_name.delete(0,tk.END)
        self.address.delete(0,tk.END)
    def show_all(self):
        self.c.execute(f"SELECT id,* FROM {self.table}")
        self.c.fetchall()
    def __del__(self):
        self.conn.close()
    def loop(self):
        tk.mainloop()
root = tk.Tk()
start = myGui(root)
start.loop()