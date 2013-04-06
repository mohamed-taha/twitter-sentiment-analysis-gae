from google.appengine.ext import ndb

from keys import SUPPORTED_CATEGORY, RANKS


class SentimentScore(ndb.Model):
    """
    Sentiment Score, Article as parent
    """
    sentiment_score     = ndb.FloatProperty()
    rank                = ndb.StringProperty(choices=[RANKS], required=True)
    category            = ndb.StringProperty(choices=[SUPPORTED_CATEGORY], required=True)

class Article(ndb.Model):
    """
    Article model
    """
    article_id      = ndb.StringProperty(required=True)
    article_text    = ndb.TextProperty(indexed=False)
    raw_content     = ndb.JsonProperty(indexed=False)
    scores          = ndb.StructuredProperty(SentimentScore, repeated=True)

    #def updateScores(self, category, score):
        #"""
        #"""
        #if not self.scores:
            #self.scores = []


class SentimentClassifier(ndb.Model):
    """
    Sentiment Classifier
    """
    category        = ndb.StringProperty(choices=[SUPPORTED_CATEGORY], required=True)
    classifier      = ndb.BlobProperty()

