import csv

def reader(path,filename):
    f = open(path +'/'+ filename, 'r')
    reader = csv.reader(f)
    return reader


def getTimestamp(reader):
    timestamp = []
    count = 0
    for row in reader: 
        timestamp.append(row[3])
        count += 1
    return timestamp,count