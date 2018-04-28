"""
    Contributors:
    Carlos
    Mustii 

"""
import Auth as AuthKeys
import tweepy
import json
import xlwt

book = xlwt.Workbook()
sh = book.add_sheet("1")
auth = tweepy.OAuthHandler(AuthKeys.consumer_key, AuthKeys.consumer_secret)
auth.set_access_token(AuthKeys.access_token, AuthKeys.access_token_secret)
api = tweepy.API(auth)
user = api.get_user('Spotify')
public_tweets = api.home_timeline()
sh.write(0,0,"Tweet text")
sh.write(0,1,"Date")
count = 1


for status in tweepy.Cursor(api.user_timeline, id='Spotify').items(3000):
    date = str(status.created_at)
    sh.write(count,0,status.text)
    sh.write(count,1,date)
    if count == 5:
        break 
    count += 1

book.save('simple.xls')