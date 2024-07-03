import plotly.graph_objects as go
import pandas as pd
import numpy as np


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'], high=df['AAPL.High'],
                low=df['AAPL.Low'], close=df['AAPL.Close'])
                      ])

fig.update_layout(
    title='The Great Recession',
    yaxis_title='AAPL Stock',
    shapes = [dict(
        x0='2016-12-09', x1='2016-12-09', y0=0, y1=1, xref='x', yref='paper',
        line_width=2)],
    annotations=[dict(
        x='2016-12-09', y=0.05, xref='x', yref='paper',
        showarrow=False, xanchor='left', text='Increase Period Begins')]
)

class DailyAverage:
    def __init__(self , df):
        df = pd.read_csv('https://raw.githubusercontent.com')
        df['vals'] = np.random.randint(1, 6, df.shape[0])

# output
print(df.groupby(df.index.strftime("%j").mean()))
print(df.groupby(df.index.strftime("%m%d")).mean())
fig.show()