import customtkinter as ctk
import tkinter.messagebox as tkmb
from logincode import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("640x640")
root.title("Login/Sign up Page")

def login(param):
    new_window = ctk.CTkToplevel(root)
    dbpass = check_user(param[2])
    if dbpass == None:
        tkmb.askquestion(title="Account not found",message="That username was not found. Create a new account instead of logging in.")
    if hash(param[3]) == dbpass:
        tkmb.showinfo(title="Login Successful",message="You have logged in Successfully")
        ctk.CTkLabel(new_window,text="GeeksforGeeks is best for learning ANYTHING !!").pack()
    elif hash(param[3]) != dbpass:
        tkmb.showwarning(title='Wrong password',message='Please check your password')

label = ctk.CTkLabel(root,text="Login or Sign Up")
label.pack(pady=20)

frame1 = ctk.CTkFrame(master=root)
frame1.pack(pady=20,padx=20,fill='both',expand=True)

label = ctk.CTkLabel(master=frame1,text='Login')
label.pack(pady=12,padx=10)

frame2 = ctk.CTkFrame(master=root)
frame2.pack(pady=20,padx=20,fill='both',expand=True)

label = ctk.CTkLabel(master=frame2,text='Sign Up')
label.pack(pady=12,padx=10)

user_entry= ctk.CTkEntry(master=frame1,placeholder_text="Username")
user_entry.pack(pady=12,padx=10)

user_pass= ctk.CTkEntry(master=frame1,placeholder_text="Password",show="*")
user_pass.pack(pady=12,padx=10)

user_entry= ctk.CTkEntry(master=frame2,placeholder_text="Username")
user_entry.pack(pady=12,padx=10)

user_pass= ctk.CTkEntry(master=frame2,placeholder_text="Password",show="*")
user_pass.pack(pady=12,padx=10)

firstname = ctk.CTkEntry(master=frame2, placeholder_text="First Name")
firstname.pack(pady=12, padx=20)

lastname = ctk.CTkEntry(master=frame2,placeholder_text="Last Name")
lastname.pack(pady=12, padx=20)

user_entry= ctk.CTkEntry(master=frame2,placeholder_text="Username")
user_entry.pack(pady=12,padx=10)

user_pass= ctk.CTkEntry(master=frame2,placeholder_text="Password",show="*")
user_pass.pack(pady=12,padx=10)

params = (firstname.get(), lastname.get(), user_entry.get(), user_pass.get())

print("hi")
print(params)

button1 = ctk.CTkButton(master=frame1,text='Login',command=login(params))
button1.pack(pady=12,padx=10)

button2 = ctk.CTkButton(master=frame2,text='Sign Up',command=login(params))
button2.pack(pady=12,padx=10)

# create_table()

# insert_new(params)

show_table()

conn.close()


root.mainloop()
