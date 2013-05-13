
import json
from google.appengine.ext import ndb


from models import SentimentScore, Article
from views import BaseHandler


class Bootstrap(BaseHandler):
    """
    create init data-set
    """
    def get(self):
        articles = [
            Article(article_id="320633498148945900",
                    article_text="I plan to watch evil dead next week",
                    scores=[SentimentScore(category="movie",
                                           rank="positive")]),
            Article(article_id="320633492411121664",
                article_text="all I ask for in life is to see Evil Dead",
                scores=[SentimentScore(category="movie",
                    rank="positive")]),
            Article(article_id="320635199845187600",
                article_text="Boston pizza's cheesesteak sandwiches though HighlyRecommed",
                scores=[SentimentScore(category="movie",
                    rank="positive")]),
            Article(article_id="320634367607197700",
                article_text="whenever me and Troy are home alone we always order Boston pizza no matter what",
                scores=[SentimentScore(category="restaurant",
                    rank="positive")]),
            Article(article_id="320633407723950080",
                article_text="I love Boston pizza",
                scores=[SentimentScore(category="restaurant",
                    rank="positive")]),
        ]
        ndb.put_multi(articles)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps("save %d articles" % len(articles)))

