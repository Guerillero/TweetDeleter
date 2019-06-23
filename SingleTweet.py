import tweepy
from secret import *

tweetInQuestion = 1142133432698454018

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

tweet = api.get_status(tweetInQuestion)

print(tweet._json)
