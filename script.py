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

batch_of_tweets = 1
batch_of_users = 1
path = ""
numberOfUsers = 1
sample_user_data = 15
user_filename = "users.csv"
tweet_filename = "tweets.csv"
wait = False
###
# NOTE: 
##

checkIfSaved = CU.createUsers(user_filename,numberOfRetrivels=numberOfUsers,wait=wait,batch_of_users=batch_of_users) # this line creates the users excel file

if checkIfSaved:
    raise "couldn't save to file"

file_users = reader(path,user_filename) # opens the file and reads the csv
users, count = getUsers(file_users) # gets the users and their counts
users = [users[random.randrange(len(users))] for item in range(sample_user_data)] # samples randomly the users
## Create tweets
CT.createTweetsFile(tweet_filename,users,wait=wait,batch_of_tweets=batch_of_tweets) # creates the tweets files
# # plotly.tools.set_credentials_file(username= auth.plotyUsername, api_key=auth.plotyAPIKey)

# # timestamp, count = getTimestamp(file)
# # print(Emotions.getEmotions(arrayOfEmotions=["send the tweets over here"])) # takes an array of emotions


