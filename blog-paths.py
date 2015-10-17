import utils
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
utils.addAccount("test", "123")

dict = {"test":123}
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
        return render_template("/home.html")
            

@app.route("/register", methods = ["POST"])
def register():
    
    return render_template("register.html")

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

@app.route("/settings")
@app.route("/settings/<username>", methods = ["GET", "POST"])
def settings(username):
    print("1")
    if request.method == "POST":
        username = str(request.form["user"])
        if str(dict[username]) == str(request.form["oldpass"]):
            if str(request.form["pass1"]) == str(request.form["pass2"]):
                dict[username] = str(request.form["pass1"])
                return render_template("settings.html", username = username, text = "Password successfully changed")
            else:
                return render_template("settings.html", username = username, text = "New password does not match")
        else:
            return render_template("settings.html", username = username, text = "Current password incorrect")
    else:
        return render_template("settings.html", username = username)


@app.route("/feed")
@app.route("/feed/<username>")
def feed(username):
    return render_template("feed.html", username = username)

if __name__ == "__main__":
    app.debug = True
    app.run()
    
