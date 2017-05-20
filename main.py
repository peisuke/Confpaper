#coding: UTF-8
from requests_oauthlib import OAuth1Session
import json
import config 

twitter = OAuth1Session(config.CONSUMER_KEY, config.CONSUMER_SECRET, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

params = {}
req = twitter.get("https://api.twitter.com/1.1/statuses/home_timeline.json", params = params)

timeline = json.loads(req.text)

for tweet in timeline:
  print(tweet["text"])
