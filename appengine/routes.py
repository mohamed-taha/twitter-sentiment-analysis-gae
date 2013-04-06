from webapp2 import Route

ROUTES = [
    Route('/nltk'   , handler='views.nltker.nltkTestPage'),
    Route('/search' , handler='views.search.SearchHandler'),
]

