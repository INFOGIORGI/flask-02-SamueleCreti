from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html", titolo="Welcome")

@app.route("/about")
def about():
    return render_template("about.html", titolo="About")

@app.route("/contact")
def contact():
    return render_template("contact.html", titolo="Contact")


if __name__ == '__main__':
    app.run(debug=True)