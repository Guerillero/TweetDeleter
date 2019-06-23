import os
import json
import tweepy
import time
import settings
from secret import *

def deleter(tw, idNo):
    if tw.user.screen_name != settings.username:
        if tw.retweeted == True:
            print("Unretweeted")
            api.unretweet(idNo)
        else:
            1 == 1
    elif tw.text[:2] == "RT":
        print("Unretweeted (old style retweet)")
        print(entry["id"])
        api.unretweet(idNo)
    elif tw.favorite_count + tw.retweet_count < settings.lowerBound:
        print("RT: " + str(tw.retweet_count) + " Fave: " + str(tw.favorite_count))
        print("Deleted")
        api.destroy_status(idNo)
    else:
        print("RT: " + str(tw.retweet_count) + " Fave: " + str(tw.favorite_count))
        print(idNo)

def fetch(idNumber):
    try:
        tweet = api.get_status(idNumber)
    except tweepy.error.RateLimitError:
        print("Rate Limit")
        time.sleep(520)
        fetch(idNumber)
    except tweepy.error.TweepError:
        1 == 1
    else:
        deleter(tweet, idNumber)

PATH_IN = r"A:\Documents\Documents\GitHub\twitter\data"
FILES_IN = os.listdir(PATH_IN)

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

for file in FILES_IN:
    print(file)
    fin_file = open(PATH_IN + "\\" + file, 'r')
    fin = json.load(fin_file)
    for entry in fin:
        fetch(entry["id"])
