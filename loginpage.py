import tkinter as tk
from logincode import *

root = tk.Tk()
root.geometry("960x640")
root.title("Login Page")
root.configure(bg='#8F00FF')

root.mainloop()

create_table()

params = get_inputs()

insert_new(params)

show_table()

conn.close()
