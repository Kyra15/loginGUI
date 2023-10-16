import sqlite3
import pandas as pd
import tkinter.messagebox as tkmb

conn = sqlite3.connect('test_database')
c = conn.cursor()


def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS tanklogin
                ([user_id] INTEGER PRIMARY KEY AUTOINCREMENT, 
                [firstname] TEXT, 
                [lastname] TEXT, 
                [username] TEXT, 
                [password] TEXT)
                ''')


def delete_table():
    c.execute("DROP TABLE tanklogin")


def get_inputs():
    fname = input("First Name: ")
    while not fname.isalpha():
        fname = input("First Name: ")
    lname = input("Last Name: ")
    while not lname.isalpha():
        lname = input("First Name: ")
    usern = input("Username: ")
    psswd = hash(input("Password: "))
    return fname, lname, usern, psswd


def insert_new(parameters):
    c.execute('INSERT INTO tanklogin (firstname, lastname, username, password) VALUES (?, ?, ?, ?)', parameters)
    conn.commit()


def check_user(user):
    c.execute("SELECT password FROM tanklogin WHERE username = ?", (str(user),))
    return c.fetchone()

def signup(param):
    dbpass = check_user(param[2])
    if dbpass == None:
        insert_new(param)
        tkmb.showinfo(title="Signup Successful", message="You have signed up successfully")
        # root.destroy()
        with open("mainpage.py") as f:
            exec(f.read())
    else:
        tkmb.showwarning("Invalid username", "That username is already taken, please choose a new one")


def login(param):
    print(param)
    dbpass = check_user(param[2])
    print(hash(param[3]))
    print(dbpass)
    if dbpass == None:
        tkmb.showwarning(title="Account not found",message="That username was not found.")
    if hash(param[3]) == dbpass:
        tkmb.showinfo(title="Login Successful",message="You have logged in successfully")
        # root.destroy()
        with open("mainpage.py") as f:
            exec(f.read())
    elif hash(param[3]) != dbpass:
        tkmb.showwarning(title='Wrong password',message='Please check your password')


# def check_pswd(user, psswd):
#     password_de = fernet.decrypt(psswd).decode()
#     c.execute('''SELECT * FROM tanklogin WHERE EXISTS 
#               (SELECT password FROM tanklogin WHERE 
#               username = usern 
#               AND password = password_de)''')
    


def show_table():
    c.execute('SELECT * FROM tanklogin')
    df = pd.DataFrame(c.fetchall(), columns=['user_id', 'firstname', 'lastname', 'username', 'password'])
    print(df)

