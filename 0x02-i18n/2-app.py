#!/usr/bin/env python3
"""A simple flask app
"""

from flask import Flask, render_template, request
from flask_babel import Babel

# Define configuration settings as constants
class Config(object):
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

# Create the Flask app instance
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

# Define the locale selector function
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# Define the main route
@app.route('/')
def index():
    return render_template('2-index.html')

# Run the app if executed directly
if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
