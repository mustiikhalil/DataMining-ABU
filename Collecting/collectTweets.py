import Auth as AuthKeys
import tweepy
import pandas as pd
from time import mktime
from langdetect import detect

def createTweetsFile(filename,users,wait,batch_of_tweets):

    if type(users) is not list:
        raise ValueError('Expecting an array')

    book = pd.DataFrame(columns=['ID','Tweet','Timestamp','date'])
    auth = tweepy.OAuthHandler(AuthKeys.consumer_key, AuthKeys.consumer_secret)
    auth.set_access_token(AuthKeys.access_token, AuthKeys.access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=wait)
    counter = 1
    try:
        while empty(users):
            id = api.get_user(users.pop())
            for tweet in tweepy.Cursor(api.user_timeline, id = id.id, count = batch_of_tweets).items():
                try:
                    if detect(tweet.text) == "en" and len(tweet.text) > 100:
                        date = str(tweet.created_at)
                        timestamp = mktime(tweet.created_at.timetuple())
                        book = book.append({'ID': tweet.id,'Tweet': " ".join(tweet.text.split()),'Timestamp':timestamp,"date":date}, ignore_index=True)
                        counter += 1
                except:
                    print("not in language")

    except tweepy.TweepError, e:
        print "TweepError raised, ignoring and continuing."
        print e

        if not book.empty:
            book.to_csv(filename, encoding='utf-8', index=False)
            return True
        else:
            return False

    book.to_csv(filename, encoding='utf-8', index=False)
    return True


def test():
    print("testing import")


def empty(users):
    return not (len(users) == 0)

