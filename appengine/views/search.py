from views import BaseHandler

class SearchHandler(BaseHandler):

    def get(self):
        context = {'message': 'Hello, world!'}
        self.render_response('search.html', **context)

