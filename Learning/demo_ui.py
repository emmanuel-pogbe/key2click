import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image,ImageTk
from pynput.keyboard import GlobalHotKeys
from pynput.mouse import Listener
import time

class myGui:
    def __init__(self):
        self.default_position = (10,10)
        self.root = tk.Tk()
        self.root.title("Key2Click")
        # self.root.attributes("-topmost",True)
        # self.root.overrideredirect(True)
        self.root.geometry("500x500")
        self.root.iconbitmap("./Learning/click icon.ico")

        self.main = tk.LabelFrame(master=self.root,border=0) #Everything stays inside here
        self.header = tk.LabelFrame(master=self.main,border=0)
        self.main_label = tk.Label(master=self.header,text="Key2Click",font="Calibri 20 bold")
        self.x = Image.open("./Learning/help icon.png").resize((25,25))
        self.help_icon = ImageTk.PhotoImage(self.x)
        self.icon = tk.Label(master=self.header,image=self.help_icon,fg="blue",cursor="hand2")
        self.icon.bind("<Button-1>",self.show_help) #When icon is clicked, call show_help()
        
        self.main_label.grid(row=0,column=0)
        self.icon.grid(row=0,column=1,padx=5)
        self.header.grid(row=0,column=0,columnspan=3)
        # self.root.config(cursor="crosshair") #Can be useful later
        
        self.create_shortcut = tk.Button(master=self.main,text="Select point",command=self.add_map_point) #Select point button
        self.selected_point = tk.Label(master=self.main) #Displays the point that was selected, may be removed

        self.create_shortcut.grid(row=2,column=1,pady=(0,20)) 
        self.selected_point.grid(row=1,column=1)
        
        #Area for collecting the shortcut keybind
        self.shortcut_entry_frame = tk.LabelFrame(master=self.main,borderwidth=0,border=0)  
        self.enter_shortcut = tk.Label(master=self.shortcut_entry_frame,text="Enter shortcut") #Label describing it
        self.enter_shortcut.grid(row=0,column=0,padx=(0,5))
        self.shortcut_entry = tk.Entry(master=self.shortcut_entry_frame) #Entry for it
        self.shortcut_entry.grid(row=0,column=1)
        self.shortcut_entry_frame.grid(row=3,column=0,columnspan=3,pady=(0,10))
    
        self.shortcut_set_to = tk.Label(master=self.main)

        self.add_shortcut = tk.Button(master=self.main,text="Add")
        self.add_shortcut.grid(row=4,column=1,pady=(0,20))

        #Section that contains working shortcuts
        self.shortcuts = tk.LabelFrame(master=self.main,border=0,highlightthickness=0,relief='flat')
        self.working_shortcuts = tk.Label(master=self.shortcuts,text="Loaded shortcuts",font="Calibri 16")
        self.working_shortcuts.pack()
        
        self.shortcut_list = tk.LabelFrame(master=self.shortcuts,border=0,highlightthickness=0,relief='flat')
        self.shortcut_list.pack(pady=10,fill=tk.BOTH,expand=True)
        self.scrollbar = tk.Scrollbar(master=self.shortcut_list)
        self.scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

        self.shortcuts_listbox = tk.Listbox(master=self.shortcut_list,yscrollcommand=self.scrollbar.set,width=50,highlightthickness=0)
        self.shortcuts_listbox.pack(fill=tk.X,expand=True)
        self.scrollbar.config(command=self.shortcuts_listbox.yview)
        self.shortcuts.grid(row=5,column=0,columnspan=3)
        
        #Options for Opening json file, deleting selected shortcut and editing shortcut
        self.options = tk.LabelFrame(master=self.main,border=0) 
        self.open_saved = tk.Button(master=self.options,text="Open saved")
        self.delete_shortcut = tk.Button(master=self.options,text="Delete selected")
        self.edit_shortcut = tk.Button(master=self.options,text="Edit selected")
        self.open_saved.grid(row=0,column=0,padx=10)
        self.delete_shortcut.grid(row=0,column=1,padx=10)
        self.edit_shortcut.grid(row=0,column=2,padx=10)
        self.options.grid(row=6,column=0,columnspan=3,pady=10)

        self.main.pack()
        self.root.mainloop()
    def show_help(self,event=None):
        help = """Key2Click can help you use keyboard shortcuts to click on points on your screen
        1. Click on "Create a shortcut"
        2. Select a point on your screen
        3. Type out the shortcut in the shortcut bar(e.g ctrl+f)
        4. Press "Add shortcut" and you'll be able to use the shortcut to click on that point
        """
        messagebox.showinfo("How to",help)
    def on_click(self,x,y,button,pressed):
        self.default_position = x,y
        return False
    def add_map_point(self):  #WIll probably refactor this later
        messagebox.showinfo("Note","Click at a point where you want to set a shortcut\n(after closing this message box of course)")
        self.main.pack_forget() #Take away stuff from the screen
        self.root.deiconify()  # Ensure window is not minimized
        self.root.lift()       # Bring window to front (AI suggested this part)
        self.root.focus_force() #I don't know, but AI suggested this part
        self.root.attributes("-fullscreen", True)
        self.root.overrideredirect(True)
        self.root.attributes("-alpha", 0.2) #Transparency
        self.root.config(cursor="crosshair")
        self.root.update() #AI suggested this part
        with Listener(on_click=self.on_click) as l:
            l.join()
        coordinate_x, coordinate_y = self.default_position
        self.main.pack() #Bring back stuff to the screen
        self.root.attributes("-fullscreen", False)
        self.root.geometry("500x500")
        self.root.overrideredirect(False)
        self.root.attributes("-alpha", 1)
        self.root.config(cursor="")  # Set back to normal
        self.selected_point.config(text=f"Coordinates -> {coordinate_x},{coordinate_y}")
    def open_file(self):
        self.filename = filedialog.askopenfilename(title="Select a file",filetypes=(("json files","*.json")))
        try:
            with open(self.filename,"r") as shortcuts:
                self.shorts = shortcuts.read()
        except:
            print("Couldn't read file")
start = myGui()
