#!/usr/bin/env python3
"""3. Parametrize templates"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """class for supported languages and timezone"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """select a language translation to use for that request:"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """renders the 3-index.html"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run()
