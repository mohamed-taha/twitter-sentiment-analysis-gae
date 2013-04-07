from views import BaseHandler

import json

import pipeline

class TrainHandler(BaseHandler):

    def get(self):

        pipeline.ClassifierTrainingPipeline().start()
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps("training pipeline kicked off"))

