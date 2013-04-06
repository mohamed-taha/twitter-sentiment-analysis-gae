import os

from webapp2 import WSGIApplication

from routes import ROUTES

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))

CONFIG = {
    'webapp2_extras.jinja2' : {
        'template_path': os.path.join(CURRENT_PATH, 'templates')
    },
}

APP = WSGIApplication(ROUTES, debug=True, config=CONFIG)

