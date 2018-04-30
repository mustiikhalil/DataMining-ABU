"""
    Contributors:
    Carlos
    Mustii 

"""
import Auth as AuthKeys
import tweepy
import json
import xlwt
from time import mktime

book = xlwt.Workbook()
sh = book.add_sheet("1")
auth = tweepy.OAuthHandler(AuthKeys.consumer_key, AuthKeys.consumer_secret)
auth.set_access_token(AuthKeys.access_token, AuthKeys.access_token_secret)
api = tweepy.API(auth) #, wait_on_rate_limit=True)

sh.write(0,0,"Account")
sh.write(0,1,"Date")
sh.write(0,2,"name")
sh.write(0,3,"timestamp")
count = 1
id = api.get_user("Spotify")
try:
    for followers in tweepy.Cursor(api.followers, id = id.id, count = 200).items():
        date = str(followers.created_at)
        timestamp = mktime(followers.created_at.timetuple())
        sh.write(count,2,followers.name)
        sh.write(count,0,followers.screen_name)
        sh.write(count,1,date)
        sh.write(count,3,timestamp)
        count += 1

except tweepy.TweepError, e:
    print "TweepError raised, ignoring and continuing."
    print e

book.save('users1.xls')