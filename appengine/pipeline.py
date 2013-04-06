"""
pipeline
"""
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
    for (words, sentiment) in tweets:
        all_words.extend(words)
    return all_words


def entry_map(entity):
    """
    convert entity into list
    """
    for score in entity.scores:
        yield (score.category, (entity.raw_content, score.sentiment_score))

def entry_reduce(key, values):
    word_features = get_word_features(get_words_in_tweets(values))
    def extract_features(document):
        document_words = set(document)
        features = {}
        for word in word_features:
            features['contains(%s)' % word] = (word in document_words)
        return features
    training_set = apply_features(extract_features, values)
    classifier = nltk.classify.NaiveBayesClassifier.train(training_set)
    yield pickle.dumps(classifier)

class ClassifierTrainingPipeline(base_handler.PipelineBase):
	"""
	the pipeline to train classifier
	"""
	def run(self, shards):
	    yield mapreduce_pipeline.MapperPipeline(
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