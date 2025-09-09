import tkinter as tk
from PIL import Image,ImageTk

root = tk.Tk()
path_images = "./Learning/tkinter/images" 
root.title("Image viewer")
root.iconbitmap(f"{path_images}/click icon.ico")

img1 = ImageTk.PhotoImage(Image.open(f"{path_images}/image1.png").resize((500,500)))
img2 = ImageTk.PhotoImage(Image.open(f"{path_images}/image2.png").resize((500,500)))
img3 = ImageTk.PhotoImage(Image.open(f"{path_images}/image3.png").resize((500,500)))
img4 = ImageTk.PhotoImage(Image.open(f"{path_images}/image4.png").resize((500,500)))
img5 = ImageTk.PhotoImage(Image.open(f"{path_images}/image5.png").resize((500,500)))

image_list = [img1,img2,img3,img4,img5]  #List containing all the images
status = tk.Label(root,text=f"Image 1 of {len(image_list)}",border=1, anchor="e",relief="sunken")
current_img = 1 #Global variable to work with the list
def update_status():
    status.config(text=f"Image {current_img} of {len(image_list)}")
def go_back(image_no): #Function for going back
    my_label.config(image=image_list[image_no-1]) #Using config function to change widget properties
    global current_img
    current_img -= 1
    if current_img <= 1:
        back.config(state="disabled") #Disable back button if we get to the first image
    if current_img < len(image_list):
        front.config(state="normal") #Enable front button if we are not on the last image
    update_status()
def go_forward(image_no):
    my_label.config(image=image_list[image_no-1])  
    global current_img 
    current_img += 1
    if current_img > 1:
        back.config(state="normal") #Enable back button if we are not on the first image
    if current_img >= len(image_list):
        front.config(state="disabled") #Disable front button if we are on the last image
    update_status()
my_label = tk.Label(root,image=img1)
my_label.grid(row=0,column=0,columnspan=3)

back = tk.Button(root,text="<=",command=lambda: go_back(current_img-1),state=tk.DISABLED) #Back button starts off as disabled
front = tk.Button(root,text="=>",command=lambda: go_forward(current_img+1))
exit = tk.Button(root,text="Exit",command=root.quit)

back.grid(row=1,column=0)
front.grid(row=1,column=2,pady=10)
exit.grid(row=1,column=1)
status.grid(row=2,column=0,columnspan=3,sticky="we")

root.mainloop()