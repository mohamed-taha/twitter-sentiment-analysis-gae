import os

from webapp2 import WSGIApplication

from routes import ROUTES

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))

APP = WSGIApplication(ROUTES, debug=True)

