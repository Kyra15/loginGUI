# import sqlite3
# import pandas as pd

# def get_inputs():
#     fname = input("First Name: ")
#     while not fname.isalpha():
#         fname = input("First Name: ")
#     lname = input("Last Name: ")
#     while not lname.isalpha():
#         lname = input("First Name: ")
#     usern = input("Username: ")
#     psswd = hash(input("Password: "))
#     return fname, lname, usern, psswd

# def createtable():
#     c.execute('''CREATE TABLE IF NOT EXISTS tanklogin
#             ([user_id] INTEGER PRIMARY KEY AUTOINCREMENT, 
#             [firstname] TEXT, 
#             [lastname] TEXT, 
#             [username] TEXT, 
#             [password] TEXT)
#             ''')


# def deletetable():
#     c.execute("DROP TABLE tanklogin")


# conn = sqlite3.connect('test_database')
# c = conn.cursor()

# createtable()

# parameters = get_inputs()

# c.execute('INSERT INTO tanklogin (firstname, lastname, username, password) VALUES (?, ?, ?, ?)', parameters)
# conn.commit()

# c.execute('SELECT * FROM tanklogin')
# df = pd.DataFrame(c.fetchall(), columns=['user_id', 'firstname', 'lastname', 'username', 'password'])
# print(df)

# conn.close()
