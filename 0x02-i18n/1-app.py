#!/usr/bin/env python3
"""basic Flask app + babel extension"""


from flask import Flask, render_template, request
from flask_babel import Babel
import babel



app = Flask(__name__)
babel = Babel(app)

class Config:
    LANGUAGES = ['en', 'fr']
    TIME_ZONE = "UTC"
    DEFAULT_LANGUAGE = 'en'

app.config.from_object(Config)

@app.route("/")
def index():
    """render template index.html"""
    return render_template("1-index.html")

if __name__ == '__main__':
    app.run(debug=True)