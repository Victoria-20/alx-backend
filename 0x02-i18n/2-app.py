#!/usr/bin/env python3
"""2. Get locale from request"""
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


def get_locale():
    """Select language translation to use for each request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app)  # initialize Babel
babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    """renders the 2-index.html"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
