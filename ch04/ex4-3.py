# API를 통해 트윗 하나를 등록

from twitter import *

access_token = '[Access Token]'
access_token_secret = '[Access Token Secret]'
consumer_key = '[Consumer Key]'
consumer_secret = '[Consumer Secret]'

t = Twitter(auth=OAuth(access_token, access_token_secret,
                       consumer_key, consumer_secret))
statusUpdate = t.statuses.update(status='Hello, world!')
print(statusUpdate)
