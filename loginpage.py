import customtkinter as ctk
# from logincode import *

ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("960x640")
root.title("Login Page")


def login():
    username = "Geeks"
    # pre-defined password
    password = "12345"
    new_window = ctk.CTkToplevel(root)

    new_window.title("New Window")

    new_window.geometry("350x150")
    # if user_entry.get() == username and user_pass.get() == password:
    #     tkmb.showinfo(title="Login Successful",
    #                   message="You have logged in Successfully")
    # ctk.CTkLabel(new_window,
    #              text="GeeksforGeeks is best \
    # for learning ANYTHING !!").pack()


label = ctk.CTkLabel(root, text="This is the main UI page")

label.pack(pady=20)

# Create a frame
frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=40,
fill='both', expand=True)

# Set the label inside the frame
label = ctk.CTkLabel(master=frame,
text='Modern Login System UI')
label.pack(pady=12, padx=10)

# Create the text box for taking
# username input from user
user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
user_entry.pack(pady=12, padx=10)

# Create a text box for taking
# password input from user
user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
user_pass.pack(pady=12, padx=10)

# Create a login button to login
button = ctk.CTkButton(master=frame, text='Login', command=login)
button.pack(pady=12, padx=10)

# Create a remember me checkbox
checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me')
checkbox.pack(pady=12, padx=10)

root.mainloop()

# create_table()
#
# params = get_inputs()
#
# insert_new(params)
#
# show_table()
#
# conn.close()
