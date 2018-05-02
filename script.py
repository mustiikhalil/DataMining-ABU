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
tweet_filename = "tweets_2.csv"
emotion_file = "emotions_2.csv"
wait = True
batch_Emotion = 4
###
# NOTE: 
##

# checkIfSaved = CU.createUsers(user_filename,numberOfRetrivels=numberOfUsers,wait=wait,batch_of_users=batch_of_users) # this line creates the users excel file

# if not checkIfSaved:
#     raise "couldn't save to file"

# ## READS THE USERS.CSV
file_users = reader(path,user_filename) # opens the file and reads the csv
users,user_timestamp,count = getUsers(file_users) # gets the users and their counts
users = [users[random.randrange(len(users))] for item in range(sample_user_data)] # samples randomly the users

##
# ## Create tweets
##

checkIfSaved = CT.createTweetsFile(tweet_filename,users,wait=wait,batch_of_tweets=batch_of_tweets) # creates the tweets files

if not checkIfSaved:
    raise "couldn't save to file"

file_tweets = reader(path,tweet_filename)
tweets, tweet_timestamp, ids, count = getTweets(file_tweets)

Emotions.detect(tweets,tweet_timestamp,ids,batch_Emotion,emotion_file)

file_emotions = reader(path,emotion_file)
ID, timestamp, anger, joy, sadness, fear, surprise, count = getEmotions(file_emotions)

# TimestampVis(len(user_timestamp),user_timestamp)
# plot(timestamp,anger,'anger','anger-his')
# plot(timestamp,joy,'joy','joy-his')
# plot(timestamp,sadness,'sadness','sadness-his')
# plot(timestamp,fear,'fear','fear-his')
# plot(timestamp,surprise,'surprise','surprise-his')
fullplot(timestamp,anger,joy,sadness,fear,surprise)
