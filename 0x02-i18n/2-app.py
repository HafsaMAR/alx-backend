#!/usr/bin/env python3
"""basic Flask app + babel extension"""

import babel
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

class Config:
    """
    Config class
    """
    LANGUAGES = ['en', 'fr']
    TIME_ZONE = "UTC"
    DEFAULT_LANGUAGE = 'en'

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route("/", methods=['GET'], strict_slashes=False)
def index():
    """render template index.html"""
    return render_template("1-index.html")

if __name__ == '__main__':
    app.run(debug=True)