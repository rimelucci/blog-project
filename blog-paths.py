import utils
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route("/")
def intro():
    return render_template("home.html")

@app.route("/login", methods = ["POST"])
def login():
    if str(request.form["button"]) == "Log in!":
        username = str(request.form["username"])
        if utils.pwordAuth(username, str(request.form["password"])):
            return redirect('/feed/' + username)
        else:
            return render_template("/home.html", text = "Username/Password does not match")
    else:
        return render_template("/register.html")

@app.route("/register", methods = ["GET", "POST"])
def register():
    if str(request.form["button"]) == "Register!":
        if utils.unameAuth(str(request.form["username"])) != True:
            utils.addAccount(str(request.form["username"]), str(request.form["password"]), str(request.form["firstname"]), str(request.form["lastname"]))
            utils.editInfo(str(request.form["username"]), str(request.form["paragraph_text"]))
            return redirect('/feed/' + str(request.form["username"]))
        else:
            return render_template("/register.html", text = "this username already exists")
    else:
        return render_template("/home.html")
@app.route("/allfriends")
def allfriends():
    return render_template("allfriends.html")

@app.route("/settings")
@app.route("/settings/<username>", methods = ["GET", "POST"])
def settings(username):
    print("1")
    if request.method == "POST":
        the_response = utils.changePword(str(request.form["user"]), str(request.form["oldpass"]), str(request.form["pass1"]), str(request.form["pass2"]))
        return render_template("settings.html", username = username, the_response = the_response)
    else:
        return render_template("settings.html", username = username)


@app.route("/feed")
@app.route("/feed/<username>", methods = ["GET", "POST"])
def feed(username):
    print(len(utils.showPosts("test")))
    print(request.method == "POST")
    if request.method == "POST":
        print("1")
        print(request.form["title"])
        print(request.form["paragraph_text"])
        utils.addPost(username, str(request.form["title"]), "sub", str(request.form["paragraph_text"]))
    return render_template("feed.html", username = username, posts = utils.showPosts(username), name = utils.findName(username), info = utils.showInfo(username))

if __name__ == "__main__":
    app.debug = True
    app.run()
    
