"""
    Contributors:
    Carlos
    Mustii 

"""

import os
import sys

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

plotly.tools.set_credentials_file(username= auth.plotyUsername, api_key=auth.plotyAPIKey)
file = reader("Collecting","users.csv")
timestamp, count = getTimestamp(file)
# print(Emotions.getEmotions(arrayOfEmotions=["send the tweets over here"])) # takes an array of emotions


