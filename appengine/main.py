import os

from webapp2 import WSGIApplication

from routes import ROUTES

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))

CONFIG = {
    'webapp2_extras.jinja2' : {
        'template_path': os.path.join(CURRENT_PATH, 'templates')
    },
}

JINJA_DEBUG = True

def enable_jinja2_debugging():
    """Enables blacklisted modules that help Jinja2 debugging.
        regarding the ImportError, read:
        http://jinja.pocoo.org/docs/faq/#my-tracebacks-look-weird-what-s-happening
    """
    if not JINJA_DEBUG:
        return
    try:
        from google.appengine.tools.dev_appserver import HardenedModulesHook
        HardenedModulesHook._WHITE_LIST_C_MODULES += ['_ctypes', 'gestalt']
    except ImportError:
        pass # not available on production environment, but we may still want DEBUG on



enable_jinja2_debugging()

APP = WSGIApplication(ROUTES, debug=True, config=CONFIG)

