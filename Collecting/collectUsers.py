import Auth as AuthKeys
import tweepy
import pandas as pd
from time import mktime

def createUsers(filename,numberOfRetrivels,wait,batch_of_users): 
    if numberOfRetrivels == 0:
        return 0
    
    book = pd.DataFrame(columns=['Account','Name','Date','timestamp'])
    auth = tweepy.OAuthHandler(AuthKeys.consumer_key, AuthKeys.consumer_secret)
    auth.set_access_token(AuthKeys.access_token, AuthKeys.access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=wait)
    id = api.get_user("Spotify")
    
    try:
        for followers in tweepy.Cursor(api.followers, id = id.id, count = batch_of_users).items():
            date = str(followers.created_at)
            timestamp = mktime(followers.created_at.timetuple())
            book = book.append({'Account': followers.screen_name,'Name':followers.name,'Date':date,"timestamp":timestamp}, ignore_index=True)
            if numberOfRetrivels == 0:
                break
            numberOfRetrivels -= 1

    except tweepy.TweepError, e:
        print "TweepError raised, ignoring and continuing."
        print e
        print book.empty
        if not book.empty:
            book.to_csv(filename, encoding='utf-8', index=False)
            return True
        else:
            return False
    book.to_csv(filename, encoding='utf-8', index=False)
    return True


   