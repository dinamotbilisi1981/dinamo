# import tkinter as tk

# tk.Tk().title("Python and MySQL")
# tk.Button(text="Click Me").pack()
# tk.mainloop()


# import tkinter as tk

# w = tk.Tk()
# tk.Label(w, text="Name").grid(row=0, column=0)
# tk.Entry(w).grid(row=0, column=1)
# tk.Label(w, text="Age").grid(row=1, column=0)
# tk.Entry(w).grid(row=1, column=1)
# w.mainloop()



import tkinter as tk
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="py_db"
)
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100))")

# Functions
def add_user():
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name_entry.get(), email_entry.get()))
    conn.commit()

def show_users():
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print(row)

# GUI
w = tk.Tk()
w.title("User Entry")

tk.Label(w, text="Name").grid(row=0, column=0)
tk.Label(w, text="Email").grid(row=1, column=0)

name_entry = tk.Entry(w)
email_entry = tk.Entry(w)
name_entry.grid(row=0, column=1)
email_entry.grid(row=1, column=1)

tk.Button(w, text="Add", command=add_user).grid(row=2, column=0)
tk.Button(w, text="Show All", command=show_users).grid(row=2, column=1)

w.mainloop()