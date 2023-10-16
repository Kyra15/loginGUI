#import sqlite3, hashlib, pandas, and tkinter message box
import sqlite3
import hashlib
import pandas as pd
import tkinter.messagebox as tkmb

# define current user
CurrentLoggedInUser = ""

# start SQL database connection
conn = sqlite3.connect('test_database')
c = conn.cursor()

# create table with SQL
def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS tanklogin
                ([user_id] INTEGER PRIMARY KEY AUTOINCREMENT, 
                [firstname] TEXT, 
                [lastname] TEXT, 
                [username] TEXT, 
                [password] TEXT)
                ''')

# delete table function if needed
def delete_table():
    c.execute("DROP TABLE tanklogin")

# returns list of the first name and last name of the person who is currently logged in
def get_current_user_name():
    c.execute('SELECT firstname, lastname FROM tanklogin WHERE username = ?', (CurrentLoggedInUser,))
    return list(c.fetchone())

# inserts a new row given a list of parameters (first name, last name, username, and password)
def insert_new(parameters):
    c.execute('INSERT INTO tanklogin (firstname, lastname, username, password) VALUES (?, ?, ?, ?)', tuple(parameters))
    conn.commit()

# returns the password of the username given
def check_user(user):
    c.execute("SELECT password FROM tanklogin WHERE username = ?", (str(user),))
    return c.fetchone()

# calls check_user using username given, hashes the password given, if the value from check_user is none, 
# password is unique and valid, and the user's info is entered into the table using insert_new
# if check_user value is not none, gives an error message and prompts user to re-enter
def signup(param):
    dbpass = check_user(param[2])
    hashed = hashlib.md5(param[3].encode())
    param[3] = str(hashed.hexdigest())
    if dbpass == None:
        insert_new(param)
        tkmb.showinfo(title="Signup Successful", message="You have signed up successfully")
    else:
        tkmb.showwarning("Invalid username", "That username is already taken, please choose a new one")

# calls check_user using the username like signup function and hashes the password
# if the value from check_user is none, that account doesn't exist, 
# if the password given and the password from the database match, 
# then the login is successful, the window is the destroyed, and the user is brought to the main page
# if the password doesn't match, then there's a warning that says to recheck the password
def login(param, root):
    global CurrentLoggedInUser
    # print("in login function",param)
    dbpass = check_user(param[0])
    hashed1 = hashlib.md5(param[1].encode())
    param[1] = str(hashed1.hexdigest())
    # print("hashed1",param[1])
    # print("dbpass",dbpass[0])
    if dbpass[0] == None:
        tkmb.showwarning(title="Account not found",message="That username was not found.")
    if param[1] == dbpass[0]:
        tkmb.showinfo(title="Login Successful",message="You have logged in successfully")
        CurrentLoggedInUser = param[0]
        # print("in login", CurrentLoggedInUser)
        root.destroy()
        with open("mainpage.py") as f:
            exec(f.read())
    elif param[1] != dbpass[0]:
        tkmb.showwarning(title='Wrong password',message='Please check your password')
    
# show table for debugging purposes
# def show_table():
#     c.execute('SELECT * FROM tanklogin')
#     df = pd.DataFrame(c.fetchall(), columns=['user_id', 'firstname', 'lastname', 'username', 'password'])
#     print(df)

