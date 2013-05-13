"""
pipeline
"""
import logging
import pickle
import nltk

from nltk.probability import FreqDist
from nltk.classify.util import apply_features

from mapreduce import base_handler
from mapreduce import mapreduce_pipeline


def get_word_features(word_list):
    word_list = FreqDist(word_list)
    word_features = word_list.keys()
    return word_features

def get_words_in_tweets(tweets):
    all_words = []
    for tweet in tweets:
        if type(tweet) == tuple:
            logging.error(tweet[0])
            all_words.extend(tweet[0])
    return all_words


def entry_map(entity):
    """
    convert entity into list
    """
    for score in entity.scores:
        yield (score.category, (entity.article_text, score.rank))

def entry_reduce(key, raw_values):

    values = []
    for raw_value in raw_values:
        logging.error(raw_value)
        logging.error(type(raw_value))
        value = eval(raw_value)
        values.append(value)

    tweets = []
    for(words,sentiment)in values:
        words_filtered=[e.lower() for e in words.split() if len(e)>=3]
        tweets.append((words_filtered ,sentiment))

    word_features = get_word_features(get_words_in_tweets(tweets))

    def extract_features(document):
        logging.error(document)
        document_words = set(document)
        features = {}
        for word in word_features:
            logging.error(word)
            features['contains(%s)' % word] = (word in document_words)
        return features

    training_set = apply_features(extract_features, tweets)
    logging.error(training_set)
    classifier = nltk.classify.NaiveBayesClassifier.train(training_set)
    setattr(classifier, 'category', key)
    yield pickle.dumps(classifier)

class ClassifierTrainingPipeline(base_handler.PipelineBase):
	"""
	the pipeline to train classifier
	"""
	def run(self, shards=4):
	    yield mapreduce_pipeline.MapreducePipeline(
            "Train Classifier",
            "pipeline.entry_map",
            "pipeline.entry_reduce",
            "mapreduce.input_readers.DatastoreInputReader",
            output_writer_spec="mapreduce.output_writers.BlobstoreOutputWriter",
            mapper_params={
                "input_reader" : {
                    "entity_kind": "models.Article",
                    "namespace":   "",
                }},
            reducer_params={"mime_type": "text/plain",},
            shards=shards
        )