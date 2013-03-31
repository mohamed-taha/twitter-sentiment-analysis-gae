import logging
import json
import webapp2

import nltk

from nltk.probability import FreqDist, ELEProbDist
from nltk.classify.util import apply_features,accuracy
from google.appengine.api import urlfetch

# Test project for NLTK for app engine
# copyright (c) 2012 Client Side Web
# for the public domain.
# NOTE: prior to running, download NLTK for App Engine and PyYAML libs and place in project root.

def bag_of_words(words):
    """
    turn words into tuples
    """
    return dict([word, True] for word in words)
    
def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
        all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

pos_tweets=[('I love this car','positive'), 
    ('This view is amazing','positive'),
    ('I feel great this morning','positive'),
    ('I am so excited about the concert','positive'),
    ('He is my best friend','positive')]

neg_tweets=[('I do not like this car','negative'),
    ('This view is horrible','negative'),
    ('I feel tired this morning','negative'),
    ('I am not looking forward to the concert','negative'),
    ('He is my enemy','negative')]

tweets=[]
for(words,sentiment)in pos_tweets+neg_tweets:
    words_filtered=[e.lower() for e in words.split() if len(e)>=3]
    tweets.append((words_filtered,sentiment))

word_features = get_word_features(get_words_in_tweets(tweets))

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

training_set = apply_features(extract_features, tweets)

classifier = nltk.classify.NaiveBayesClassifier.train(training_set)


class nltkTestPage(webapp2.RequestHandler):
    def get(self):
        response       = urlfetch.fetch("http://search.twitter.com/search.json?q=saskatoon%20weather")
        vendastaTweets = [tweet.get('text') for tweet in json.loads(response.content).get('results', [])]
        results        = [{'text': tweet, 'result':classifier.classify(bag_of_words(nltk.word_tokenize(tweet)))} for tweet in vendastaTweets]
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(results))

app = webapp2.WSGIApplication([('/nltk', nltkTestPage)], debug=True)
