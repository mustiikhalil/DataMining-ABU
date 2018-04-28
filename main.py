"""
    Contributors:
    Carlos
    Mustii 

"""
import Auth as AuthKeys
import tweepy
import json
import xlwt
import json
import ast
from time import mktime

book = xlwt.Workbook()
sh = book.add_sheet("1")
auth = tweepy.OAuthHandler(AuthKeys.consumer_key, AuthKeys.consumer_secret)
auth.set_access_token(AuthKeys.access_token, AuthKeys.access_token_secret)
api = tweepy.API(auth)
public_tweets = api.home_timeline()
sh.write(0,0,"Account")
sh.write(0,1,"Date")
sh.write(0,2,"name")
sh.write(0,3,"timestamp")
count = 1
id = api.get_user("Spotify")

for status in tweepy.Cursor(api.followers, id = id.id, count = 50).items():
    date = str(status.created_at)
    timestamp = mktime(status.created_at.timetuple())
    sh.write(count,2,status.name)
    sh.write(count,0,status.screen_name)
    sh.write(count,1,date)
    sh.write(count,3,timestamp)
        
    if count == 5:
        break 
    count += 1
    

book.save('simple.xls')