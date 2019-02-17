import urllib2, os
from flask import Flask, render_template, request, redirect, flash, url_for
#from util import translate, feed_help, datamuse

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def home():
        return render_template("index.html")


@app.route("/project")
def project():
        return render_template("projects.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
