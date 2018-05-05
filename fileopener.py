import pandas as pd
import csv


def reader(path,filename):
    f = open(path + filename, 'r')
    reader = csv.reader(f)
    return reader


def getUsers(reader):
    timestamp = []
    users = []
    count = 0
    for row in reader: 
        timestamp.append(row[3]) 
        users.append(row[0])
        count += 1
    return users[1:],timestamp[1:], count


def getTweets(reader):
    tweets = []
    timestamp = []
    ids = []
    date = []
    count = 0
    for row in reader: 
        ids.append(row[0])
        tweets.append(row[1])
        timestamp.append(row[2])
        date.append(row[3])
        count += 1
    return tweets[1:],timestamp[1:],ids[1:],date[1:], count


def getEmotions(reader):
    ID = []
    timestamp = []
    date = []
    anger = []
    joy = []
    sadness = []
    fear = []
    surprise = []
    timeOfDay = []
    count = 0
    for row in reader: 
        ID.append(row[0])
        timestamp.append(row[1])
        date.append(row[2])
        anger.append(row[3])
        joy.append(row[4])
        sadness.append(row[5])
        fear.append(row[6])
        surprise.append(row[7])
        timeOfDay.append(row[8])
        count += 1
    return ID[1:], timestamp[1:],date[1:] , anger[1:], joy[1:], sadness[1:], fear[1:], surprise[1:],timeOfDay[1:], count


def reader_sort(filename,sortby):
    df = pd.read_csv(filename)
    df = df.sort_values(sortby)
    df.to_csv(filename[:-4]+ '_sorted.csv', index=False)

def convert_to_csv(xlsxfilename,csvfilename,sheetnumber):
    data_xls = pd.read_excel(xlsxfilename, sheetnumber, index_col=None)
    return data_xls.to_csv(csvfilename, encoding='utf-8', index=False)
