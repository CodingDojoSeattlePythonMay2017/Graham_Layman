from flask import Flask, render_template, redirect, request
app=Flask(__name__)

@app.route("/")
def landingPage():
    return render_template("index.html")

@app.route("/response", methods=["POST"])
def response():
    print "got stuff"
    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form["comment"]
    print location
    print language
    print name
    return render_template("/response.html", name=name, location=location,language=language,comment=comment)


app.run(debug=True)
