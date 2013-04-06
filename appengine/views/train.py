from views import BaseHandler

import pipeline

class TrainHandler(BaseHandler):

    def get(self):

        pipeline.ClassifierTrainingPipeline().start()
        context = {'message': 'Hello, world!'}
        self.render_response('search.html', **context)

