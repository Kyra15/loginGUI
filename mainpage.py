import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("640x800")
root.title("Login/Sign up Page")


label = ctk.CTkLabel(root,text="This is the main UI page")

label.pack(pady=20)

vidframe = ctk.CTkFrame(root)
vidframe.pack(vidframe.pack(pady=20,padx=40,fill='both',expand=True))


