"""
    Contributors:
    Carlos
    Mustii 

"""
import Auth as AuthKeys
import tweepy
from database import Database

data = Database()

auth = tweepy.OAuthHandler(AuthKeys.consumer_key, AuthKeys.consumer_secret)
auth.set_access_token(AuthKeys.access_token, AuthKeys.access_token_secret)

api = tweepy.API(auth)


user = api.get_user('twitter')
print(user)

public_tweets = api.home_timeline()

for status in tweepy.Cursor(api.user_timeline, id='twitter').items(3000):
    print(status)