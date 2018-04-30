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
