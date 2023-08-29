#!/usr/bin/env python3
"""A simple Flask app
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _, get_locale, get_timezone
import pytz.exceptions
import locale
from datetime import datetime
from pytz import timezone

# ... (other imports and classes)

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

# Define the user data
USERS = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Define a function to get the current time in user's timezone
def get_current_time():
    user_tz = g.user.get('timezone', app.config['BABEL_DEFAULT_TIMEZONE'])
    tz = pytz.timezone(user_tz)
    now = datetime.now(tz)
    time_format = "%b %d, %Y, %I:%M:%S %p"
    return now.strftime(time_format)

# Attach user and time to global context before each request
@app.before_request
def before_request():
    g.user = get_user()
    g.time = get_current_time()

# ... (other route functions)

# Run the app if executed directly
if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)

