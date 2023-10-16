#import customtkinter and functioncode file
import customtkinter as ctk
from funccode import *

#define variables to get login info and sign up info
def getloginformvalues():
    # debug statements
    # print("Login button pressed", login_user_entry, login_user_pass)
    # print("getloginform values user name:",login_user_entry.get())
    # print("getloginform values user pass:",login_user_pass.get())
    param = [login_user_entry.get(), login_user_pass.get()]
    login(param, root)

def getsignupformvalues():
    # debug statements
    # print("Signup Button Pressed")
    # print("first name:",firstname.get())
    # print("last name:",lastname.get())
    # print("user name:",signup_user_entry.get())
    # print("user pass:",signup_user_pass.get())
    param = [firstname.get(), lastname.get(), signup_user_entry.get(), signup_user_pass.get()]
    signup(param)


#set up tkinter window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("960x640")
root.title("Login/Sign up Page")

# title label
labeltitle = ctk.CTkLabel(root,text="Login or Sign Up", font=("Segoe UI", 32))
labeltitle.pack(pady=20)

# frame 1(login)
frame1 = ctk.CTkFrame(master=root)
frame1.pack(pady=20,padx=20,fill='both',expand=True, side='left')

labellog = ctk.CTkLabel(master=frame1,text='Login', font=("Segoe UI", 20))
labellog.pack(pady=12,padx=10)

login_user_entry= ctk.CTkEntry(master=frame1,placeholder_text="Username")
login_user_entry.pack(pady=12,padx=10)

login_user_pass= ctk.CTkEntry(master=frame1,placeholder_text="Password",show="*")
login_user_pass.pack(pady=12,padx=10)

button1 = ctk.CTkButton(master=frame1,text='Login',hover=False,command=getloginformvalues)
button1.pack(pady=12,padx=10)

#frame 2 (signup)
frame2 = ctk.CTkFrame(master=root)
frame2.pack(pady=20,padx=20,fill='both',expand=True, side='left')

labelsign = ctk.CTkLabel(master=frame2,text='Sign Up', font=("Segoe UI", 20))
labelsign.pack(pady=12,padx=10)

firstname = ctk.CTkEntry(master=frame2, placeholder_text="First Name")
firstname.pack(pady=12, padx=10)

lastname = ctk.CTkEntry(master=frame2,placeholder_text="Last Name")
lastname.pack(pady=12, padx=10)

signup_user_entry= ctk.CTkEntry(master=frame2,placeholder_text="Username")
signup_user_entry.pack(pady=12,padx=10)

signup_user_pass= ctk.CTkEntry(master=frame2,placeholder_text="Password",show="*")
signup_user_pass.pack(pady=12,padx=10)

button2 = ctk.CTkButton(master=frame2,text='Sign Up',hover=False,command=getsignupformvalues)
button2.pack(pady=12,padx=10)

root.mainloop()

conn.close()