import plotly
import plotly.plotly as py
from plotly.graph_objs import *
import numpy as np


def TimestampVis(count,timestamp):
    x = np.linspace(0,1,count)

    trace0 = Scatter(
        x=x,
        y=sorted(
            timestamp
        )
    )

    # plots a line 
    data = Data([trace0])
    py.plot(data, filename = 'basic-line')

    # histogram of data
    Histo = [Histogram(x=timestamp)]
    py.plot(Histo, filename='basic histogram')

def plot(point,data,filename,Histogram_name):

    trace0 = Scatter(
        x=point,
        y=data,
        name=filename
    )

    # plots a line 
    data = Data([trace0])
    py.plot(data, filename = filename)

    # histogram of data
    Histo = [Histogram(x=point)]
    py.plot(Histo, filename=Histogram_name)


def fullplot(timestamp,anger,joy,sadness,fear,surprise):
    anger = Scatter(
        x=timestamp,
        y=anger,
        name="anger"
    )
    joy = Scatter(
        x=timestamp,
        y=joy,
        name="joy"
    )
    sadness = Scatter(
        x=timestamp,
        y=sadness,
        name="sadness"
    )
    fear = Scatter(
        x=timestamp,
        y=fear,
        name="fear"
    )
    surprise = Scatter(
        x=timestamp,
        y=surprise,
        name="surprise"
    )
    # plots a line 
    data = Data([anger,joy,sadness,fear,surprise])
    py.plot(data, filename = 'full-plot')
    # histogram of data
    Histo = [Histogram(x=anger),Histogram(x=joy),Histogram(x=sadness),Histogram(x=fear),Histogram(x=surprise)]
    py.plot(Histo, filename='full histogram')


def printNumberOfTimesInTweets(timeOfDay):
    countNight = 0
    countAfternoon = 0
    countMorning = 0
    countEvening = 0
    print len(timeOfDay)
    for time in timeOfDay:
        if time == "Night":
            countNight += 1
        elif time == 'Afternoon':
            countAfternoon += 1
        elif time == 'Morning':
            countMorning += 1
        else:
            countEvening += 1

    print 'Night',countNight
    print 'Afternoon',countAfternoon
    print 'Morning',countMorning
    print 'Evening',countEvening