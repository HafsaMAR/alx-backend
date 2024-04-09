#!/usr/bin/env python3
"""basic Flask app"""


from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    """render template index.html"""
    return render_template("0-index.html")

if __name__ == '__main__':
    app.run(debug=True)