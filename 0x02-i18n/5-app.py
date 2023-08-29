#!/usr/bin/env python3
"""A simple Flask app
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

# Define the user data
USERS = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Create the Flask app instance
app = Flask(__name__)

# Configure the Flask app
class Config(object):
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
app.config.from_object(Config)

# Disable strict slashes in URLs
app.url_map.strict_slashes = False

# Initialize Babel extension
babel = Babel(app)

# Define a function to get the user from the query parameter
def get_user():
    login_id = request.args.get('login_as')
    return USERS.get(int(login_id)) if login_id and int(login_id) in USERS else None

# Attach user to global context before each request
@app.before_request
def before_request():
    g.user = get_user()

# Define the locale selector for Babel
@babel.localeselector
def get_locale():
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# Define the main route
@app.route('/')
def index():
    return render_template('5-index.html')

# Run the app if executed directly
if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
