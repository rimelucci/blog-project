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
    c.execute("CREATE TABLE posts (id integer, uname text, post text, time text)")
    c.execute("CREATE TABLE comments (id integer, uname text, comment text, time text)")
    c.execute("CREATE TABLE posts (id integer, uname text)")
    conn.commit()

def findID():
    ids = c.execute("SELECT id FROM posts")
    max = 0
    for r in ids:
        id = r[0]
        if (id > max):
            max = id
    return max+1

def addPost(uname, post):
    c.execute("INSERT INTO posts VALUES (?, ?, ?, ?);", (findID(), uname, post, displayDate()))
    conn.commit()

def showPost(ID):
    post = c.execute("SELECT post FROM posts WHERE id = "+str(ID)+";")
    for r in post:
        return r[0]
def showPosts(uname):
    posts = c.execute("SELECT post FROM posts WHERE uname = '"+uname+"';")
    list = []
    for r in posts:
        list.append(r[0])
    return list
print(showPosts("Milo"))
def displayDate():
    import datetime
    return str(datetime.datetime.now())

def printDate(d):
    d = d.split(" ")
    date = ""

    time = d[1].split(":")
    day = d[0].split("-")
    
    date += day[1]+"/"+day[2]+"/"+day[0]+" at "
    date += time[0]+":"+time[1]
    return date
 
print(printDate(displayDate()))
