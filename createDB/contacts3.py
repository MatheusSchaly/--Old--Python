import sqlite3

db = sqlite3.connect("contacts.sqlite")

name = input("Enter a name to be searched: ")

for row in db.execute("SELECT * FROM contacts WHERE name LIKE ?", (name,)):
    print(row)

db.close()
