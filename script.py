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
user = "cnn" # the pool of users to target
batch_of_tweets = 200 # number tweets per request
batch_of_users = 200 # number of users per request
path = "data/" # path of data
numberOfUsers = 3000 # number of users needed
sample_user_data = 30  # number of random users picked to get the tweets
user_filename = "users_new.csv"
sort_user_filename = "users_new_sorted.csv"
tweet_filename = "tweets_new.csv"
sort_tweet_filename = 'tweets_new_sorted.csv'
emotion_file = "emotions_complete.csv"

wait = False
batch_Emotion = 4
###
# NOTE: 
##

checkIfSaved = CU.createUsers(user,user_filename,numberOfRetrivels=numberOfUsers,wait=wait,batch_of_users=batch_of_users) # this line creates the users excel file

if not checkIfSaved:
    raise "couldn't save to file"

# ## READS THE USERS.CSV

reader_sort(user_filename,"timestamp")
file_users = reader(path,sort_user_filename) # opens the file and reads the csv
users,user_timestamp,count = getUsers(file_users) # gets the users and their counts
users = [users[random.randrange(len(users))] for item in range(sample_user_data)] # samples randomly the users

# #
## Create tweets
#

checkIfSaved = CT.createTweetsFile(tweet_filename,users,wait=wait,batch_of_tweets=batch_of_tweets) # creates the tweets files

if not checkIfSaved:
    raise "couldn't save to file"

reader_sort(tweet_filename,'ID')

file_tweets = reader(path,sort_tweet_filename)
tweets, tweet_timestamp, ids, tweet_date, count = getTweets(file_tweets)

Emotions.detect(tweets,tweet_timestamp,tweet_date,ids,batch_Emotion,emotion_file)

file_emotions = reader(path,emotion_file)
ID, timestamp, date, anger, joy, sadness, fear, surprise,timeOfDay, count = getEmotions(file_emotions)

printNumberOfTimesInTweets(timeOfDay)
TimestampVis(len(user_timestamp),user_timestamp)
plot(date,anger,'anger','anger-his')
plot(date,joy,'joy','joy-his')
plot(date,sadness,'sadness','sadness-his')
plot(date,fear,'fear','fear-his')
plot(date,surprise,'surprise','surprise-his')
fullplot(date,anger,joy,sadness,fear,surprise)
