import csv
import plotly
import plotly.plotly as py
from plotly.graph_objs import *
import numpy as np

def reader():
    timestamp = []
    count = 0
    with open('users.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader: 
            timestamp.append(row[3])
            count += 1
    return timestamp,count


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
