from flask import Flask, redirect, url_for, render_template, request, session, flash
#webbrowser, time, easygui, tkinter


"""
home page
login - user will enter  their butt status in the form
   user then directed to mayhem
logout - user must logout to end session. (session data is then erased)
about page

"""

app = Flask(__name__)
app.secret_key = "encrptionKey" 

@app.route("/") #path to access root page
def home():
    return render_template("index.html")

@app.route("/login", methods = ["POST", "GET"]) #path to access root page
def login():
    if request.method == "POST":
        user = request.form["nm"] #user is the input of the form
        session["user"] = user    #create session with form input
        return redirect(url_for("butt"))
    else:
        if "user" in session:
            return redirect(url_for("butt"))
        return render_template("login.html")



@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/butt_status", methods = ["POST", "GET"])
def butt():
    if "user" in session:
        user = session["user"] #if user has made a login, redirect to mayhem.html
        return render_template("mayhem.html", butt_status = user)
    else:
        return redirect(url_for("login")) #else back to login page

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("You have been logged out", "info") #flash a message after logging out of session. flash type = info
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug = True)