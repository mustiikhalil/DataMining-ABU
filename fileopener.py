import pandas
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


def convert_to_csv(xlsxfilename,csvfilename,sheetnumber):
    data_xls = pandas.read_excel(xlsxfilename, sheetnumber, index_col=None)
    return data_xls.to_csv(csvfilename, encoding='utf-8', index=False)
