# 4.5 트위터

from twitter import *

access_token = '[Access Token]'
access_token_secret = '[Access Token Secret]'
consumer_key = '[Consumer Key]'
consumer_secret = '[Consumer Secret]'

t = Twitter(auth=OAuth(access_token, access_token_secret,
                       consumer_key, consumer_secret))
pythonTweets = t.search.tweets(q = "#python")
print(pythonTweets)
