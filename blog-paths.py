from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

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
    
