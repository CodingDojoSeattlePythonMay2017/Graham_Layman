from flask import Flask, render_template, redirect, request, flash, session, url_for
import re
import datetime
app=Flask(__name__)
app.secret_key = "F"

@app.route("/")
def landingPage():
    return render_template("index.html")

@app.route("/post", methods=["POST"])
def validate():
    #I moved all the validation tests to their own functions to keep this clean
    if not allFields():
        flash("Please fill out all fields.")
        return redirect("/")
    if not valNam():
        return redirect("/")
    if not valEmail():
        return redirect("/")
    if not valDate():
        return redirect("/")
    if not PwMatch():
        return redirect("/")
    if not PwVal():
        return redirect("/")
    return render_template("success.html")

@app.route("/back", methods=["POST"])
def back():
    return redirect("/")

def valNam():
    namReg = re.compile(r'\d')
    if namReg.search(request.form["firstName"]) or namReg.search(request.form["lastName"]):
        flash("Names should not contain any numbers.")
        return False
    return True

def PwMatch():
    if request.form["password"] == request.form["confirmPW"]:
        return True
    flash("Password confirmation did not match password.")
    return False

def PwVal():
    PW_REGEX = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$')
    if not PW_REGEX.match(request.form["password"]):
        flash("Password must be at least 8 characters long and contain at least one number, one special character and one uppercase letter.")
        return False
    return True

def valDate():
    if len(request.form["bDay"]) > 10:
        flash("Please enter a valid date")
        return False
    print request.form["bDay"]
    year = ""
    day = ""
    month = ""
    #date format is YYYY-MM-DD
    for x,y in enumerate(request.form["bDay"]):
        if x < 4:
            year += y
        elif 4 < x < 7:
            month += y
        elif 7 < x:
            day += y
    if not datetime.datetime(year=int(year), month=int(month),day=int(day)) <= datetime.datetime(year=2010, month = 1, day=1):
        flash("I'm sorry but either you're from the future or you are not old enough to be using this site.")
        return False
    elif not datetime.datetime(year=1897, month=1, day=1) <= datetime.datetime(year=int(year), month=int(month),day=int(day)):
        flash("It's unlikely that you're still alive to be using this site, please enter a more valid birthday")
        return False
    return True



def valEmail():
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address")
        return False
    return True

def allFields():
    if len(request.form["firstName"]) < 1:
        return False
    if len(request.form["lastName"]) < 1:
        return False
    if len(request.form["email"]) < 1:
        return False
    if len(request.form["bDay"]) < 1:
        return False
    if len(request.form["password"]) < 1:
        return False
    if len(request.form["confirmPW"]) < 1:
        return False
    return True


app.run(debug=True)
