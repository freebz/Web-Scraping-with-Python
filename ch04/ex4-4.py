# 트윗 목록을 요청할 때 가져올 숫자를 정함

from twitter import *

access_token = '[Access Token]'
access_token_secret = '[Access Token Secret]'
consumer_key = '[Consumer Key]'
consumer_secret = '[Consumer Secret]'

t = Twitter(auth=OAuth(access_token, access_token_secret,
                       consumer_key, consumer_secret))
pythonStatuses = t.statuses.user_timeline(screen_name="montypython", count=5)
print(pythonStatuses)
