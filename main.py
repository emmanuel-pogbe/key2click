import os
import sys
import json
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image,ImageTk
from pynput.keyboard import HotKey
from pynput.keyboard import GlobalHotKeys
from pynput.mouse import Listener
import pyautogui
import webbrowser
class myGui:
    def __init__(self):
        self.button_fg ="#333333"

        pyautogui.FAILSAFE = False
        #Where to save shortcuts
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
        self.root.minsize(700,800)
        self.root.configure(bg="#f5f5f5")
        self.icon_path = self.resource_path("click icon.ico")
        self.root.iconbitmap(self.icon_path)
        self.root.protocol("WM_DELETE_WINDOW",self.on_close) #When closing window - call self.on_close() function

        self.main = tk.LabelFrame(master=self.root,border=0,bg="#f5f5f5") #Everything stays inside here
        self.header = tk.LabelFrame(master=self.main,border=0)
        self.main_label = tk.Label(master=self.header,text="Key2Click",font="Calibri 20 bold")
        self.help_icon = self.resource_path("help icon.png")
        self.x = Image.open(self.help_icon).resize((25,25))
        self.help_icon = ImageTk.PhotoImage(self.x)
        self.icon = tk.Label(master=self.header,image=self.help_icon,fg="blue",cursor="hand2")
        self.icon.bind("<Button-1>",self.show_help) #When icon is clicked, call show_help()
        
        self.main_label.grid(row=0,column=0)
        self.icon.grid(row=0,column=1,padx=5)
        self.header.grid(row=0,column=0,columnspan=3,pady=(5,20))
        # self.root.config(cursor="crosshair") #Can be useful later
        
        self.create_shortcut = tk.Button(master=self.main,text="Select point",command=self.add_map_point,cursor="hand2",fg=self.button_fg,bg="white") #Select point button
        self.selected_point = tk.Label(master=self.main,text="No point selected") #Displays the point that was selected, may be removed

        self.create_shortcut.grid(row=2,column=1,pady=(0,20)) 
        self.selected_point.grid(row=1,column=1)
        
        #Area for collecting the shortcut keybind
        self.shortcut_entry_frame = tk.LabelFrame(master=self.main,borderwidth=0,border=0)  
        self.enter_shortcut = tk.Label(master=self.shortcut_entry_frame,text="Enter shortcut") #Label describing it
        self.enter_shortcut.grid(row=0,column=0,padx=(0,5))
        self.shortcut_entry = tk.Entry(master=self.shortcut_entry_frame,bd=1) #Entry for it
        self.shortcut_entry.grid(row=0,column=1)
        self.shortcut_entry_frame.grid(row=3,column=0,columnspan=3,pady=(0,10))
    
        self.shortcut_set_to = tk.Label(master=self.main)

        self.add_shortcut = tk.Button(master=self.main,text="Add",command=self.add_shortcut_to_list,cursor="hand2",fg=self.button_fg,bg="white")
        self.add_shortcut.grid(row=4,column=1,pady=(0,20))

        #Section that contains working shortcuts
        self.shortcuts = tk.LabelFrame(master=self.main,border=0,highlightthickness=0,relief='flat')
        self.working_shortcuts = tk.Label(master=self.shortcuts,text="Loaded shortcuts",font="Calibri 16",border=0)
        self.working_shortcuts.pack()
        
        self.shortcut_list = tk.LabelFrame(master=self.shortcuts,border=0,highlightthickness=0,relief='flat')
        self.shortcut_list.pack(pady=10,fill=tk.BOTH,expand=True)
        self.scrollbar = tk.Scrollbar(master=self.shortcut_list)
        self.scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

        self.shortcuts_listbox = tk.Listbox(master=self.shortcut_list,yscrollcommand=self.scrollbar.set,width=50,highlightthickness=0,selectmode=tk.EXTENDED,font="Courier",border=0)
        self.shortcuts_listbox.pack(fill=tk.X,expand=True)
        self.scrollbar.config(command=self.shortcuts_listbox.yview)
        self.shortcuts.grid(row=5,column=0,columnspan=3,pady=(0,10))
        
        #Options for Opening json file, deleting selected shortcut and editing shortcut
        self.options = tk.LabelFrame(master=self.main,border=0) 
        self.open_saved = tk.Button(master=self.options,text="Open saved",command=self.open_file,cursor="hand2",fg=self.button_fg,bg="white")
        self.export_to = tk.Button(master=self.options,text="Export shortcuts",command=self.export_to_json,cursor="hand2",fg=self.button_fg,bg="white")
        self.delete_shortcut = tk.Button(master=self.options,text="Delete selected",command=self.delete_selected,cursor="hand2",fg=self.button_fg,bg="white")
        self.edit_shortcut = tk.Button(master=self.options,text="Edit Point",command=self.edit_selected_point,cursor="hand2",fg=self.button_fg,bg="white")
        self.open_saved.grid(row=0,column=0,padx=10)
        self.export_to.grid(row=0,column=1,padx=10)
        self.delete_shortcut.grid(row=0,column=2,padx=10)
        self.edit_shortcut.grid(row=0,column=3,padx=10)
        self.options.grid(row=6,column=0,columnspan=3,pady=10)

        self.start_btn = tk.Button(master=self.main,text="START",padx=10,pady=10,cursor="hand2",command=self.start_program,font="Calibri 16 bold",fg="white",bg="#019315",activeforeground="white",activebackground="#026E10")
        self.start_btn.grid(row=7,column=0,columnspan=3,padx=(10,0))

        self.github_path = self.resource_path("github logo.png")
        self.github_img = Image.open(self.github_path).resize((30,30))
        self.github_img_p = ImageTk.PhotoImage(self.github_img)

        self.footer = tk.Frame(master=self.root,relief=tk.SUNKEN,bd=2)
        footer_label = tk.Label(
            master=self.footer,
            image=self.github_img_p,
            bg="#f0f0f0",
            cursor="hand2"
        )
        footer_label.bind("<Button-1>",lambda e: self.open_url("https://github.com/emmanuel-pogbe/key2click"))
        footer_label.pack(side=tk.RIGHT,padx=5,pady=5)

        #Bring back auto_saved shortcuts
        self.auto_saved_shortcuts()

        self.main.pack()
        self.footer.pack(side=tk.BOTTOM,fill=tk.X)
        self.root.mainloop()
    
    def on_close(self):
        self.save_shortcuts() #Save shortcuts before closing file
        self.root.destroy()
    def start_program(self):
        if not self.is_running:
            if len(self.shortcuts_dictionary)>0:
                self.is_running = True
                self.start_btn.config(text="STOP",activebackground="#A50000",bg="#D10000")
                #Hide irrelevant stuff on screen first
                #Will only show loaded shortcuts
                self.selected_point.grid_forget()
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
            self.selected_point.grid(row=1,column=1)
            self.shortcut_entry_frame.grid(row=3,column=0,columnspan=3,pady=(0,10))
            self.add_shortcut.grid(row=4,column=1,pady=(0,20))
            self.options.grid(row=6,column=0,columnspan=3,pady=10)
            self.create_shortcut.grid(row=2,column=1,pady=(0,20))
            self.start_btn.config(text="START",bg="#019315",activeforeground="white",activebackground="#026E10")
            #Stop program
            self.quit_program(self.listener)
    def quit_program(self,hotkey_class):
        if hotkey_class.running:
            hotkey_class.stop()
    def show_help(self,event=None):
        help = """Key2Click can help you use keyboard shortcuts to click on points on your screen
        1. Click on "Select point"
        2. Select a point on your screen
        3. Type out the shortcut in the shortcut bar(e.g ctrl+f)
        4. Press "Add" to add the shortcut to loaded shortcuts
        5. Once done loading all your shortcuts, press 'START'
        """
        messagebox.showinfo("How to",help)
    def on_click(self,x,y,button,pressed):
        self.default_position = x,y
        return False
    def configure_selection_window(self,is_selecting):
        if is_selecting == True:
            self.main.pack_forget() #Take away stuff from the screen
            self.footer.pack_forget()
            # Get screen size and position
            size = pyautogui.size()
            width = size[0]
            height = size[1]
            
            self.root.deiconify()
            self.root.lift()
            self.root.focus_force()
            self.root.overrideredirect(True)
            self.root.geometry(f"{width}x{height}+0+0")

            self.root.update_idletasks()
            self.root.attributes("-alpha", 0.2)
            self.root.update()
            self.root.config(cursor="crosshair")
        else:
            self.root.after(100,self.main.pack)
            self.root.after(100,lambda: self.footer.pack(side=tk.BOTTOM,fill=tk.X))
            # self.main.pack() #Bring back stuff to the screen
            # self.root.attributes("-fullscreen", False)
            self.root.overrideredirect(False)
            self.root.geometry("700x800")
            self.root.attributes("-alpha", 1)
            self.root.config(cursor="")  # Set back to normal
    
    def add_map_point(self):  #Will probably refactor this later
        proceed = messagebox.askokcancel("Note","Click at a point where you want to set a shortcut\n(after clicking 'ok' of course)")
        if proceed:
            self.configure_selection_window(True)
            with Listener(on_click=self.on_click) as l:
                l.join()
            coordinate_x, coordinate_y = self.default_position
            self.configure_selection_window(False)
            self.selected_point.config(text=f"Coordinates -> {coordinate_x},{coordinate_y}")
            # self.selected_point.grid(row=1,column=1)
    def add_shortcut_to_list(self):
        if not self.default_position:
            messagebox.showinfo("Note","You have not selected a point!")
        else:
            shortcut = self.get_shortcut().lower()
            if not self.is_available(shortcut=shortcut):
                messagebox.showinfo("Note","Shortcut is already mapped to a point! Enter another one\nNote: Shortcuts are case-insensitive")
            elif not self.is_valid_shortcut(shortcut): 
                messagebox.showinfo("Note","Please enter a valid shortcut! Here are some ideas (the '+' is very important)\nctrl+f\nalt+p\nshift+1\nctrl+alt+3\nz\n9\nShortcuts are case-insensitive")
            else:
                self.insert_listbox(shortcut,self.default_position)
                self.shortcuts_dictionary[shortcut] = self.default_position
                # self.default_position = None
                # self.selected_point.grid_forget()
                self.shortcut_entry.delete(0,tk.END)
                self.save_shortcuts()
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
        selected = self.shortcuts_listbox.curselection()
        if len(selected) >= 1:
            for item in reversed(selected): #reverse the list so that we can delete from the end so as not to affec the current list
                item_string = self.shortcuts_listbox.get(item)
                self.shortcuts_listbox.delete(item)
                idx = item_string.rfind("(")
                # end_str = selected_point[idx:]  #Not needed
                start_str = item_string[:idx].strip()
                if start_str in self.shortcuts_dictionary:
                    self.shortcuts_dictionary.pop(start_str)
                self.save_shortcuts()
        else:
            messagebox.showinfo("No shortcut selected","You have not selected any shortcut to delete!")
    def open_file(self):
        screen_size = pyautogui.size()
        self.filename = filedialog.askopenfilename(
            title="Select a file",
            filetypes=[("JSON files", "*.json")]
        )
        if self.filename:
            is_corrupt = False
            try:
                with open(self.filename,"r") as shortcuts:
                    self.shorts = json.load(shortcuts)
                    duplicates_ = set()
                    for shortcut in self.shorts:
                        #If shortcut is valid and the value for the shortcut is a list and the length of the list = 2 (x and y values) and both values are integers and points are within the size of the screen
                        shortcut = shortcut.lower()
                        points = self.shorts.get(shortcut)
                        if self.is_valid_shortcut(shortcut) and type(points) == list and len(points) == 2 and all(isinstance(x,int) for x in points) and points[0]<=screen_size[0] and points[1]<=screen_size[1]:
                            if shortcut not in self.shortcuts_dictionary:
                                temp_shortcut = self.shorts.get(shortcut)
                                self.insert_listbox(shortcut,temp_shortcut)
                                self.shortcuts_dictionary[shortcut] = temp_shortcut
                            else:
                                duplicates_.add(shortcut)
                        else:
                            is_corrupt = True
                    if is_corrupt:
                        messagebox.showwarning("Error loading shortcuts","Some shortcuts were not loaded! " \
                        "Confirm that the file is formatted properly\n" \
                        "1. Ensure that all the keys are valid shortcuts\n" \
                        "2. Ensure all the values are lists\n" \
                        "3. Ensure there are only 2 elements in each list and are integers\n" \
                        f"4. Ensure the points are within the bounds of your screen size {tuple(screen_size)}"    
                        )
                    elif duplicates_:
                        messagebox.showinfo("Unloaded shortcuts",f"{duplicates_} already present in loaded shortcuts")  
            except Exception as e:
                messagebox.showerror("Read error", f"Oops! Something went wrong {e.__class__.__name__} {e}")
    def export_to_json(self):
        if len(self.shortcuts_dictionary) < 1:
            messagebox.showinfo("No loaded shortcuts","There are no loaded shortcuts to export")
        else:
            try:
                json_file = filedialog.asksaveasfile(mode="w",defaultextension="json",filetypes=[("JSON files", "*.json")],title="Export loaded shortcuts")
                if json_file:
                    json.dump(self.shortcuts_dictionary,json_file,indent=2)
                    json_file.close()
            except Exception as e:
                messagebox.showerror("Error",f"Oops! Something went wrong: {e.__class__.__name__}")
    def save_shortcuts(self):
        try:
            with open(self.config_file,"w") as sh:    
                json.dump(self.shortcuts_dictionary,sh,indent=2)
        except Exception as e:
            #What do I put here incase saving fails, probably log it or something, idk
            pass
    def get_shortcut_dictionary(self):
        all_shortcuts = self.get_all_shortcuts()
        short_dict = {
            short:self.listify(mapping) for short,mapping in (shortcut.split() for shortcut in all_shortcuts)
        }
        return short_dict
    def edit_selected_point(self):
        selected = self.shortcuts_listbox.curselection()
        if len(selected) == 1:
            self.configure_selection_window(True) #Configure screen to select a new point
            with Listener(on_click=self.on_click) as l:
                l.join()
            coordinate_x, coordinate_y = self.default_position
            self.configure_selection_window(False)
            selected_point = self.shortcuts_listbox.get(selected[0])
            idx = selected_point.rfind("(")
            # end_str = selected_point[idx:]  #Not needed
            start_str = selected_point[:idx].strip()
            self.shortcuts_listbox.delete(selected[0])
            self.shortcuts_listbox.insert(selected[0],self.format_mapping(start_str,self.default_position))
        elif len(selected) >1 :
            messagebox.showinfo("Multiple selections","You can only edit one shortcut point at a time")
        else:
            messagebox.showinfo("No shortcut selected","You have not selected any shortcut to edit!")
    def auto_saved_shortcuts(self):
        #For loading autosaved shortcuts when app is opened 
        try:
            with open(self.config_file,"r") as sh:
                shortcuts = json.load(sh)
                for short,short_position in shortcuts.items():
                    self.shortcuts_dictionary[short] = short_position
                    self.insert_listbox(short,short_position)
        except Exception as e:
            #autosave didn't work I guess, oh well
            pass
    def click_point(self,shortcut_key):
        #Using pyautogui to move to a point, and click on that point
        coordinate_x,coordinate_y = self.shortcuts_dictionary.get(shortcut_key) 
        try:
            pyautogui.moveTo(coordinate_x,coordinate_y)
            pyautogui.leftClick()
        except pyautogui.FailSafeException as e:
            pass
        except Exception as e:
             messagebox.showerror("Error",f"Something went wrong: {e.__class__.__name__} {e}")
    def is_valid_shortcut(self,s: str):
        try:
            HotKey.parse(s)
            return True
        except:
            #We can have more try except blocks in this place to make input handling more robust
            return False
    def listify(self,s: str) -> tuple: 
        #Takes string having a tuple-like structure and turns it into a tuple
        cleaned = s.strip("() ").split(",")    
        return list(int(x) for x in cleaned)
    def resource_path(self,relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)
    def open_url(self,url):
        webbrowser.open(url=url,autoraise=True)
if __name__ == "__main__":
    start = myGui()