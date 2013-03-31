import pickle

from keys import SVM, NBAYES

from nltk.classify import SvmClassifier
from nltk.classify import NaiveBayesClassifier

import models.SentimentClassifier


CLASSIFIER_TYPE_MAP = {
    SVM:    SvmClassifier,
    NBAYES: NaiveBayesClassifier
}

class Record(object):
    """
    domain object
	"""
    def __init__(self, text, value=None):
       """
       constructor
       """
       self.text  = text
       self.value = value

class TrainingSet(object):
    """
	training set
	"""
    def __init__(self, records):
       """
       constructor
       """
       self.records = records
       self._value   = None

    def value(self):
        """
		return value
		"""
        if not self._value:
           self._value = [(record.text, record.value) for record in self.records]
        return self._value


class Classifier(object):
    """
	domain object present Classifier
	"""
    def __init__(self, trainingSet=None, classifierType=NBAYES, classifier=None):
        """
        constructor
	    """
        if classifier:
            self.__classifier = classifier
        else:
            classifierClass  = CLASSIFIER_TYPE_MAP.get(classifierType)
            classifier       = classifierClass.train(trainingSet)
            self.__classifier = classifier

    @classmethod
    def load(cls, resource):
        """
		load resource
		"""
        cls(classifer=pickle.load(resource))



