import os
import json
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image,ImageTk
from pynput.keyboard import GlobalHotKeys
from pynput.mouse import Listener
import pyautogui

class myGui:
    def __init__(self):
        #Shortcuts saving variables
        self.appdata = os.getenv("APPDATA")
        self.config_dir = Path(self.appdata)/"Key2Click"
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir/"shortcuts.json"

        self.is_running = False
        self.default_position = None
        self.shortcuts_dictionary = {}
        self.root = tk.Tk()
        self.root.title("Key2Click")
        # self.root.attributes("-topmost",True)
        # self.root.overrideredirect(True)
        self.root.geometry("700x800")
        self.root.iconbitmap("./Learning/click icon.ico")
        self.root.protocol("WM_DELETE_WINDOW",self.on_close) #When closing window - call self.on_close() function

        self.main = tk.LabelFrame(master=self.root,border=0) #Everything stays inside here
        self.header = tk.LabelFrame(master=self.main,border=0)
        self.main_label = tk.Label(master=self.header,text="Key2Click",font="Calibri 20 bold")
        self.x = Image.open("./Learning/help icon.png").resize((25,25))
        self.help_icon = ImageTk.PhotoImage(self.x)
        self.icon = tk.Label(master=self.header,image=self.help_icon,fg="blue",cursor="hand2")
        self.icon.bind("<Button-1>",self.show_help) #When icon is clicked, call show_help()
        
        self.main_label.grid(row=0,column=0)
        self.icon.grid(row=0,column=1,padx=5)
        self.header.grid(row=0,column=0,columnspan=3,pady=(5,15))
        # self.root.config(cursor="crosshair") #Can be useful later
        
        self.create_shortcut = tk.Button(master=self.main,text="Select point",command=self.add_map_point,cursor="hand2") #Select point button
        self.selected_point = tk.Label(master=self.main) #Displays the point that was selected, may be removed

        self.create_shortcut.grid(row=2,column=1,pady=(0,20)) 
        # self.selected_point.grid(row=1,column=1)
        
        #Area for collecting the shortcut keybind
        self.shortcut_entry_frame = tk.LabelFrame(master=self.main,borderwidth=0,border=0)  
        self.enter_shortcut = tk.Label(master=self.shortcut_entry_frame,text="Enter shortcut") #Label describing it
        self.enter_shortcut.grid(row=0,column=0,padx=(0,5))
        self.shortcut_entry = tk.Entry(master=self.shortcut_entry_frame) #Entry for it
        self.shortcut_entry.grid(row=0,column=1)
        self.shortcut_entry_frame.grid(row=3,column=0,columnspan=3,pady=(0,10))
    
        self.shortcut_set_to = tk.Label(master=self.main)

        self.add_shortcut = tk.Button(master=self.main,text="Add",command=self.add_shortcut_to_list)
        self.add_shortcut.grid(row=4,column=1,pady=(0,20))

        #Section that contains working shortcuts
        self.shortcuts = tk.LabelFrame(master=self.main,border=0,highlightthickness=0,relief='flat')
        self.working_shortcuts = tk.Label(master=self.shortcuts,text="Loaded shortcuts",font="Calibri 16")
        self.working_shortcuts.pack()
        
        self.shortcut_list = tk.LabelFrame(master=self.shortcuts,border=0,highlightthickness=0,relief='flat')
        self.shortcut_list.pack(pady=10,fill=tk.BOTH,expand=True)
        self.scrollbar = tk.Scrollbar(master=self.shortcut_list)
        self.scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

        self.shortcuts_listbox = tk.Listbox(master=self.shortcut_list,yscrollcommand=self.scrollbar.set,width=50,highlightthickness=0,selectmode=tk.EXTENDED,font="Courier")
        self.shortcuts_listbox.pack(fill=tk.X,expand=True)
        self.scrollbar.config(command=self.shortcuts_listbox.yview)
        self.shortcuts.grid(row=5,column=0,columnspan=3)
        
        #Options for Opening json file, deleting selected shortcut and editing shortcut
        self.options = tk.LabelFrame(master=self.main,border=0) 
        self.open_saved = tk.Button(master=self.options,text="Open saved",command=self.open_file)
        self.delete_shortcut = tk.Button(master=self.options,text="Delete selected",command=self.delete_selected)
        self.edit_shortcut = tk.Button(master=self.options,text="Edit selected")
        self.open_saved.grid(row=0,column=0,padx=10)
        self.delete_shortcut.grid(row=0,column=1,padx=10)
        self.edit_shortcut.grid(row=0,column=2,padx=10)
        self.options.grid(row=6,column=0,columnspan=3,pady=10)

        self.start_btn = tk.Button(master=self.main,text="START",padx=10,pady=10,cursor="hand2",command=self.start_program,font="Calibri 16 bold")
        self.start_btn.grid(row=7,column=0,columnspan=3)

        #Bring back auto_saved shortcuts
        self.auto_saved_shortcuts()

        self.main.pack()
        self.root.mainloop()
    def on_close(self):
        self.save_shortcuts() #Save shortcuts before closing file
        self.root.destroy()
    def start_program(self):
        if not self.is_running:
            self.is_running = True
            self.start_btn.config(text="STOP")
            #Hide irrelevant stuff on screen first
            #Will only show loaded shortcuts
            self.shortcut_entry_frame.grid_forget()
            self.add_shortcut.grid_forget()
            self.create_shortcut.grid_forget()
            self.options.grid_forget()
            self.shortcuts_dictionary = self.get_shortcut_dictionary()
            self.hotkey_map = { # I love copilot so much
                short:(lambda s = short: self.click_point(s)) for short in self.shortcuts_dictionary
            }
            self.listener = GlobalHotKeys(self.hotkey_map)
            self.listener.start()
        else:
            self.is_running = False
            #Bring back stuff to the screen
            self.shortcut_entry_frame.grid(row=3,column=0,columnspan=3,pady=(0,10))
            self.add_shortcut.grid(row=4,column=1,pady=(0,20))
            self.options.grid(row=6,column=0,columnspan=3,pady=10)
            self.create_shortcut.grid(row=2,column=1,pady=(0,20))
            self.start_btn.config(text="START")
            #Stop program
            self.quit_program(self.listener)
    def quit_program(self,hotkey_class):
        if hotkey_class.running:
            hotkey_class.stop()
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
    def add_map_point(self):  #Will probably refactor this later
        messagebox.showinfo("Note","Click at a point where you want to set a shortcut\n(after closing this message box of course)")
        self.main.pack_forget() #Take away stuff from the screen
        self.root.deiconify()  # Ensure window is not minimized
        self.root.lift()       # Bring window to front (AI suggested this part)
        self.root.focus_force() #I don't know, but AI suggested this part
        self.root.attributes("-fullscreen", True)
        self.root.overrideredirect(True)
        self.root.config(cursor="crosshair") #Change to crosshair cursor
        self.root.attributes("-alpha", 0.2) #Transparency
        self.root.update() #AI suggested this part
        with Listener(on_click=self.on_click) as l:
            l.join()
        coordinate_x, coordinate_y = self.default_position
        self.root.after(100,self.main.pack)
        # self.main.pack() #Bring back stuff to the screen
        self.root.attributes("-fullscreen", False)
        self.root.geometry("700x800")
        self.root.overrideredirect(False)
        self.root.attributes("-alpha", 1)
        self.root.config(cursor="")  # Set back to normal
        self.selected_point.config(text=f"Coordinates -> {coordinate_x},{coordinate_y}")
        self.selected_point.grid(row=1,column=1)
    def add_shortcut_to_list(self):
        if not self.default_position:
            messagebox.showinfo("Note","You have not selected a point!")
        else:
            shortcut = self.get_shortcut()
            if not self.is_available(shortcut=shortcut):
                messagebox.showinfo("Note","Shortcut is already mapped to a point! Enter another one")
            elif not shortcut.strip(): 
                messagebox.showinfo("Note","Please enter a valid shortcut")
            else:
                self.insert_listbox(shortcut,self.default_position)
                self.default_position = None
                self.selected_point.grid_forget()
                self.shortcut_entry.delete(0,tk.END)
    def is_available(self,shortcut):
        #I might find a better way to do this
        all_shorts = (shortcut_info.split()[0] for shortcut_info in self.get_all_shortcuts())
        if shortcut in all_shorts:
            return False
        return True
    def get_all_shortcuts(self):
        return self.shortcuts_listbox.get(0,tk.END)
    def insert_listbox(self,shortcut,position):
        self.shortcuts_listbox.insert(0,self.format_mapping(shortcut=shortcut,position=position))
    def format_mapping(self,shortcut,position):
        return f"{shortcut.ljust(38)}({position[0]},{position[1]})" #For the sake of sakes
    def get_shortcut(self):
        shortcut = self.shortcut_entry.get()
        br = shortcut.split("+")
        for i in range(len(br)):
            br[i] = br[i].strip()
            if len(br[i])>1:
                br[i] = f"<{br[i]}>"
        return "+".join(br)
    def delete_selected(self):
        for item in reversed(self.shortcuts_listbox.curselection()): #reverse the list so that we can delete from the end so as not to affec the current list
            self.shortcuts_listbox.delete(item)
    def open_file(self):
        self.filename = filedialog.askopenfilename(
            title="Select a file",
            filetypes=[("JSON files", "*.json")]
        )
        try:
            with open(self.filename,"r") as shortcuts:
                self.shorts = json.load(shortcuts)
                for shortcut in self.shorts:
                    #Perform a check here first to determine if shortcut is valid
                    self.insert_listbox(shortcut,self.shorts.get(shortcut))
        except:
            messagebox.showerror("Read error", "Oops! Something went wrong")
    def save_shortcuts(self):
        try:
            with open(self.config_file,"w") as sh:
                
                json.dump(self.shortcuts_dictionary,sh,indent=2)
        except:
            #What do I put here incase saving fails, hmmm
            print("Unsuccessful")
            pass
    def get_shortcut_dictionary(self):
        all_shortcuts = self.get_all_shortcuts()
        short_dict = {
            short:self.listify(mapping) for short,mapping in (shortcut.split() for shortcut in all_shortcuts)
        }
        return short_dict

    def auto_saved_shortcuts(self):
        #For loading autosaved shortcuts when app is opened 
        try:
            with open(self.config_file,"r") as sh:
                shortcuts = json.load(sh)
                for short,short_position in shortcuts.items():
                    self.insert_listbox(short,short_position)
        except:
            #No autosaved shortcuts in this case
            print("I couldn't load the shortcuts :(")
        pass
    def click_point(self,shortcut_key):
        #Using pyautogui to move to a point, and click on that point
        coordinate_x,coordinate_y = self.shortcuts_dictionary[shortcut_key] 
        try:
            pyautogui.moveTo(coordinate_x,coordinate_y)
            pyautogui.leftClick()
        except:
            pass #Maybe later
    def listify(self,s: str) -> tuple: 
        #Takes string having a tuple-like structure and turns it into a tuple
        cleaned = s.strip("() ").split(",")    
        return list(int(x) for x in cleaned)
if __name__ == "__main__":
    start = myGui()