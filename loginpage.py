import customtkinter as ctk
from logincode import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("640x800")
root.title("Login/Sign up Page")

labeltitle = ctk.CTkLabel(root,text="Login or Sign Up")
labeltitle.pack(pady=20)

frame1 = ctk.CTkFrame(master=root)
frame1.pack(pady=20,padx=20,fill='both',expand=True)

labellog = ctk.CTkLabel(master=frame1,text='Login')
labellog.pack(pady=12,padx=10)

frame2 = ctk.CTkFrame(master=root)
frame2.pack(pady=20,padx=20,fill='both',expand=True)

labelsign = ctk.CTkLabel(master=frame2,text='Sign Up')
labelsign.pack(pady=12,padx=10)

user_entry= ctk.CTkEntry(master=frame1,placeholder_text="Username")
user_entry.pack(pady=12,padx=10)

user_pass= ctk.CTkEntry(master=frame1,placeholder_text="Password",show="*")
user_pass.pack(pady=12,padx=10)

firstname = ctk.CTkEntry(master=frame2, placeholder_text="First Name")
firstname.pack(pady=12, padx=10)

lastname = ctk.CTkEntry(master=frame2,placeholder_text="Last Name")
lastname.pack(pady=12, padx=10)

user_entry= ctk.CTkEntry(master=frame2,placeholder_text="Username")
user_entry.pack(pady=12,padx=10)

user_pass= ctk.CTkEntry(master=frame2,placeholder_text="Password",show="*")
user_pass.pack(pady=12,padx=10)

print(firstname.get())
print(lastname.get())
print(user_entry.get())
print(user_pass.get())

params = (firstname.get(), lastname.get(), user_entry.get(), user_pass.get())

button1 = ctk.CTkButton(master=frame1,text='Login',command=lambda:login(params))
button1.pack(pady=12,padx=10)

button2 = ctk.CTkButton(master=frame2,text='Sign Up',command=lambda:signup(params))
button2.pack(pady=12,padx=10)

root.mainloop()

conn.close()