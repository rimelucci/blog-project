import sqlite3

conn = sqlite3.connect("Data.db")
c = conn.cursor()

def pwordAuth(uname, pword):
    p = c.execute("SELECT pword FROM accounts WHERE uname = '"+uname+"';")
    for r in p:
        return r[0] == pword
    return False

def addAccount(uname, pword):
    c.execute("INSERT INTO accounts VALUES (?, ?);", (uname, pword))
    conn.commit()

def changePword(uname, oldP, newP, cNewP):
    p = c.execute("SELECT pword FROM accounts WHERE uname = '"+uname+"';")
    for r in p:
        result = r[0]
    if result != oldP:
        return "The password you input was incorrect."
    if newP != cNewP:
        return "The confirmed new password did not match."
    else:
        c.execute("UPDATE accounts SET pword = '"+newP+"' WHERE uname = '"+uname+"';")
        conn.commit()        
        return "Password successfully updated"

#+=====++ Blog Posts ++=====+#

# posts:
# (id, uname, post, time)
# 
# comments:
# (id, uname, comment, time)
#
# likes:
# (id, uname)

def setup():
    c.execute("CREATE TABLE posts (id integer, uname text, post text, time timestamp)")
    c.execute("CREATE TABLE comments (id integer, uname text, comment text, time timestamp)")
    c.execute("CREATE TABLE posts (id integer, uname text)")
    conn.commit()
