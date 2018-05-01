"""
    Contributors:
    Carlos
    Ibrahim
    Mustii 
"""

import os
import sys
import random 
sys.dont_write_bytecode = True
absFilePath = os.path.abspath(__file__)
fileDir = os.path.dirname(os.path.abspath(__file__))
collectingPath = os.path.join(fileDir, 'Collecting') 
emotionPath = os.path.join(fileDir, 'emotionDetector') 
sys.path.append(emotionPath)
sys.path.append(collectingPath)

import csv
import plotly
from visualizing import *
from fileopener import *
import emotions as Emotions
import Auth as auth
import collectTweets as CT 
import collectUsers as CU 

# plotly.tools.set_credentials_file(username= auth.plotyUsername, api_key=auth.plotyAPIKey)
batch_of_tweets = 200
batch_of_users = 200
path = ""
numberOfUsers = 1400
sample_user_data = 1
user_filename = "users.csv"
tweet_filename = "tweets.csv"
wait = True
batch_Emotion = 4
###
# NOTE: 
##

checkIfSaved = CU.createUsers(user_filename,numberOfRetrivels=numberOfUsers,wait=wait,batch_of_users=batch_of_users) # this line creates the users excel file

if not checkIfSaved:
    raise "couldn't save to file"

## READS THE USERS.CSV
file_users = reader(path,user_filename) # opens the file and reads the csv
users,user_timestamp,count = getUsers(file_users) # gets the users and their counts
users = [users[random.randrange(len(users))] for item in range(sample_user_data)] # samples randomly the users

##
# ## Create tweets
##

CT.createTweetsFile(tweet_filename,users,wait=wait,batch_of_tweets=batch_of_tweets) # creates the tweets files

file_tweets = reader(path,tweet_filename)
tweets, tweet_timestamp, ids, count = getTweets(file_tweets)

Emotions.detect(tweets,tweet_timestamp,ids,batch_Emotion,"emotions.csv")

