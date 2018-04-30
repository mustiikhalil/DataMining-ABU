"""
    Contributors:
    Carlos
    Mustii 

"""
import Auth as AuthKeys
import tweepy
import xlwt
from time import mktime

book = xlwt.Workbook()
sh = book.add_sheet("1")
auth = tweepy.OAuthHandler(AuthKeys.consumer_key, AuthKeys.consumer_secret)
auth.set_access_token(AuthKeys.access_token, AuthKeys.access_token_secret)
api = tweepy.API(auth) #, wait_on_rate_limit=True)


book.save('tweets.xls')
