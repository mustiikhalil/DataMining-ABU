"""
    Contributors:
    Carlos
    Mustii 

"""
import Auth as AuthKeys
import tweepy
from database import Database
import json
import xlwt

book = xlwt.Workbook()
sh = book.add_sheet("1")

data = Database()

auth = tweepy.OAuthHandler(AuthKeys.consumer_key, AuthKeys.consumer_secret)
auth.set_access_token(AuthKeys.access_token, AuthKeys.access_token_secret)

api = tweepy.API(auth)


user = api.get_user('Spotify')
public_tweets = api.home_timeline()
count = 0
for status in tweepy.Cursor(api.user_timeline, id='Spotify').items(3000):
    sh.write(count,0,status.text)
    if count == 5:
        break 
    count += 1

book.save('simple.xls')