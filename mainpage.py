# import customtkinter and the function code file
import customtkinter as ctk
from funccode import *

# set the name of the current user
name = str(get_current_user_name()[0]).title() + " " + str(get_current_user_name()[1]).title()
# print("main1", name)

# set up tkinter window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("960x640")
root.title("Login/Sign up Page")

label = ctk.CTkLabel(root,text=f"Welcome, {name}", font=("Segoe UI", 24))
label.pack(pady=20)

# set up frame with video
vidframe = ctk.CTkFrame(root)
vidframe.pack(pady=20,padx=20,fill='both',expand=True, side='left')
label = ctk.CTkLabel(vidframe,text=f"Live Feed")
label.pack(pady=20)

# set up frame with log
logframe = ctk.CTkFrame(root)
logframe.pack(pady=20,padx=20,fill='both',expand=True, side='bottom')
label = ctk.CTkLabel(logframe,text=f"Log")
label.pack(pady=20)

# set up frame with controls
controlsframe = ctk.CTkFrame(root)
controlsframe.pack(pady=20,padx=20,fill='both',expand=True, side='top')
label = ctk.CTkLabel(controlsframe,text=f"Controls")
label.pack(pady=20)

# set up empty frame
emptyframe = ctk.CTkFrame(root)
emptyframe.pack(pady=20,padx=20,fill='both',expand=True, side='left')
label = ctk.CTkLabel(emptyframe,text=f"Blank")
label.pack(pady=20)

root.mainloop()



