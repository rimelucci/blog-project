import sqlite3

#+=====++ Setup ++=====+#
def setup():
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    c.execute("CREATE TABLE accounts (uname text, pword text, first text, last text, info text, piclink text)")
    c.execute("CREATE TABLE posts (id integer, uname text, title text, sub text, post text, time text)")
    c.execute("CREATE TABLE comments (id integer, uname text, comment text, time text)")
    c.execute("CREATE TABLE likes (id integer, uname text)")
    conn.commit()

#+=====++ Accounts ++=====+#
def unameAuth(uname):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    accounts = c.execute("SELECT uname FROM accounts")
    for r in accounts:
        if r[0] == uname:
            return True
    return False

def pwordAuth(uname, pword):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    p = c.execute("SELECT pword FROM accounts WHERE uname = '"+uname+"';")
    for r in p:
        return r[0] == pword
    return False

def addAccount(uname, pword, first, last):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    accounts = c.execute("SELECT uname FROM accounts")
    for r in accounts:
        if r[0] == uname:
            return "This account name already exists"
    c.execute("INSERT INTO accounts VALUES (?, ?, ?, ?, ?, ?);", (uname, pword, first, last, "", ""))
    conn.commit()

def changePword(uname, oldP, newP, cNewP):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
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

def findName(uname):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    n = c.execute("SELECT first, last FROM accounts WHERE uname ='"+uname+"';")
    for r in n:
        return r[0]+" "+r[1]

def editInfo(uname, info):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    c.execute("UPDATE accounts SET info = '"+info+"' WHERE uname = '"+uname+"';")
    conn.commit()

def showInfo(uname):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    n = c.execute("SELECT info FROM accounts WHERE uname = '"+uname+"';")
    for r in n:
        return r[0]

def newPic(uname):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    c.execute("UPDATE accounts SET piclink = '"+uname+"' WHERE uname = '"+uname+"';")
    conn.commit()

def findPic(uname):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    n = c.execute("SELECT piclink FROM accounts WHERE uname = '"+uname+"';")
    for r in n:
        return r[0]
    
#+=====++ Blog Posts ++=====+#

# posts:
# (id, uname, post, title, sub, time)
# 
# comments:
# (id, uname, comment, time)
#
# likes:
# (id, uname)

def findID():
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    ids = c.execute("SELECT id FROM posts")
    max = 0
    for r in ids:
        id = r[0]
        if (id > max):
            max = id
    return max+1

def addPost(uname, title, sub, post):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    c.execute("INSERT INTO posts VALUES (?, ?, ?, ?, ?, ?);", (findID(), uname, title, sub, post, displayDate()))
    conn.commit()

def showPosts(uname):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    posts = c.execute("SELECT id, title, sub, post, time FROM posts WHERE uname = '"+uname+"';")
    list = []
    for r in posts:
        list.append(r)# ID, title, sub, post, stamp
    return list

def showPost(ID):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    post = c.execute("SELECT post FROM posts WHERE id = "+str(ID)+";")
    for r in post:
        return r[0]

def addComment(ID, uname, comment):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    c.execute("INSERT INTO comments VALUES (?, ?, ?, ?);", (ID, uname, comment, displayDate()))
    conn.commit()

def showComments(ID):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    comments = c.execute("SELECT uname, comment, time FROM comments WHERE id = "+str(ID)+";")
    list = []
    for r in comments:
        list.append(r)# uname, comment, time
    return list

def addLike(ID, uname):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    c.execute("INSERT INTO likes VALUES (?, ?);", (ID, uname))
    conn.commit()

def showLikes(ID):
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()
    likes = c.execute("SELECT uname FROM likes WHERE id = "+str(ID)+";")
    list = []
    for r in likes:
        list.append(r[0])# uname
    return list

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

