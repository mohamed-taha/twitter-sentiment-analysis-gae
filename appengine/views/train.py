from views import BaseHandler

import json

import pipeline

class TrainHandler(BaseHandler):

    def get(self):

        stage = pipeline.ClassifierTrainingPipeline()
        stage.start()
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps("training pipeline kicked off %s" % stage.pipeline_id))

