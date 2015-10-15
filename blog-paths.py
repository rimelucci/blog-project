from flask import Flask, render_template, request
app = Flask(__name__)

dict = {"test":123}

@app.route("/", methods = ["POST"])
def login():
    if str(request.form["submitting"]) == "Login_In":
        print("1");
        username = str(request.form["username"])
        if username in dict.keys():
            print("3")
            print(dict[username])
            print(request.form["password"])
            if str(dict[username]) == str(request.form["password"]):
                return render_template("/feed.html")
            else:
                return render_template("/login.html", text = "Username/Password does not match")
        else:
            return render_template("/login.html", text = "Username does not exist")
    else:
        print("2")
        return render_template("/login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

@app.route("/setting")
def setting():
    return render_template("setting.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
    
