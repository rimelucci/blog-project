import sqlite3

conn = sqlite3.connect("Data.db")
c = conn.cursor()

c.execute("INSERT INTO accounts VALUES('milo', 'password');")

conn.commit()

def pwordAuth(uname, pword):
    print c.execute("SELECT pword FROM accounts WHERE name = '"+uname+"';")


pwordAuth("milo", "pword")
