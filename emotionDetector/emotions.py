import os
import sys
import indicoio
import Auth as auth 

indicoio.config.api_key = auth.emotionsAPI

def getEmotions(arrayOfEmotions):
    return indicoio.emotion(arrayOfEmotions)