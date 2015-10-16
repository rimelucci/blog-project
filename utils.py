import sqlite3

conn = sqlite3.connect("Data.db")
c = conn.cursor()

def pwordAuth(uname, pword):
    p = c.execute("SELECT pword FROM accounts WHERE uname = '"+uname+"';")
    for r in p:
        return r[0] == pword

def addAccount(uname, pword):
    c.execute("INSERT INTO accounts VALUES (?, ?)", (uname, pword))
    conn.commit()

#def changePword(uname, oldP, newP, cNewP):
#    result = c.execute(
