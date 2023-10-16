import tkinter as tk

# Create the main application window
app = tk.Tk()
app.title("Login Page")

# Function to handle login button click
def login():
    username = username_entry.get()
    password = password_entry.get()
    # Add your authentication logic here
    print(f"Login with Username: {username}, Password: {password}")

# Function to handle sign up button click
def signup():
    username = signup_username_entry.get()
    password = signup_password_entry.get()
    # Add your sign-up logic here
    print(f"Sign Up with Username: {username}, Password: {password}")

# Create a login frame
login_frame = tk.Frame(app)
login_frame.pack(padx=10, pady=10)

# Create login widgets
login_label = tk.Label(login_frame, text="Login")
username_label = tk.Label(login_frame, text="Username")
password_label = tk.Label(login_frame, text="Password")
username_entry = tk.Entry(login_frame)
password_entry = tk.Entry(login_frame, show="*")
login_button = tk.Button(login_frame, text="Login", command=login)

# Grid layout for login widgets
login_label.grid(row=0, column=0, columnspan=2)
username_label.grid(row=1, column=0)
password_label.grid(row=2, column=0)
username_entry.grid(row=1, column=1)
password_entry.grid(row=2, column=1)
login_button.grid(row=3, column=0, columnspan=2)

# Create a sign-up frame
signup_frame = tk.Frame(app)
signup_frame.pack(padx=10, pady=10)

# Create sign-up widgets
signup_label = tk.Label(signup_frame, text="Sign Up")
signup_username_label = tk.Label(signup_frame, text="Username")
signup_password_label = tk.Label(signup_frame, text="Password")
signup_username_entry = tk.Entry(signup_frame)
signup_password_entry = tk.Entry(signup_frame, show="*")
signup_button = tk.Button(signup_frame, text="Sign Up", command=signup)

# Grid layout for sign-up widgets
signup_label.grid(row=0, column=0, columnspan=2)
signup_username_label.grid(row=1, column=0)
signup_password_label.grid(row=2, column=0)
signup_username_entry.grid(row=1, column=1)
signup_password_entry.grid(row=2, column=1)
signup_button.grid(row=3, column=0, columnspan=2)

# Start the tkinter main loop
app.mainloop()