from google.appengine.ext import ndb

from keys import SUPPORTED_CATEGORY

class Article(ndb.Model):
    """
    Article model
    """
    article_id      = ndb.StringProperty(required=True)
    article_text    = ndb.TextProperty(indexed=False)
    raw_content     = ndb.JsonProperty(indexed=False)

class SentimentScore(ndb.Model):
    """
    Sentiment Score, Article as parent
    """
    article_id          = ndb.StringProperty(required=True)
    sentiment_score     = ndb.FloatProperty(required=True)
    category            = ndb.StringProperty(choices=[SUPPORTED_CATEGORY], required=True)

class SentimentClassifier(ndb.Model):
    """
    Sentiment Classifier
    """
    category        = ndb.StringProperty(choices=[SUPPORTED_CATEGORY], required=True)
    classifier      = ndb.BlobProperty()

