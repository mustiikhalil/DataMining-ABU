import pandas
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
    count = 0
    for row in reader: 
        tweets.append(row[1])
        timestamp.append(row[2])
        ids.append(row[0])
        count += 1
    return tweets[1:],timestamp[1:],ids[1:], count


def getEmotions(reader):
    ID = []
    timestamp = []
    anger = []
    joy = []
    sadness = []
    fear = []
    surprise = []
    count = 0
    for row in reader: 
        ID.append(row[0])
        timestamp.append(row[1])
        anger.append(row[2])
        joy.append(row[3])
        sadness.append(row[4])
        fear.append(row[5])
        surprise.append(row[6])
        count += 1
    return ID[1:], timestamp[1:], anger[1:], joy[1:], sadness[1:], fear[1:], surprise[1:], count



def convert_to_csv(xlsxfilename,csvfilename,sheetnumber):
    data_xls = pandas.read_excel(xlsxfilename, sheetnumber, index_col=None)
    return data_xls.to_csv(csvfilename, encoding='utf-8', index=False)
