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
    def __init__(self, url):
        self.df = pd.read_csv(url)
        self.df['vals'] = np.random.randint(1, 6, self.df.shape[0])
        # Assuming 'Date' is a column with date information in a format that pandas can parse.
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df.set_index('Date', inplace=True)

    def average_by_day_of_year(self):
        return self.df.groupby(self.df.index.strftime("%j")).mean()

    def average_by_date(self):
        return self.df.groupby(self.df.index.strftime("%m%d")).mean()


# Usage:

# Replace 'your_url' with your actual CSV URL
your_url = 'https://raw.githubusercontent.com/user/repo/file.csv'
daily_avg = DailyAverage(your_url)
print(daily_avg.average_by_day_of_year())
print(daily_avg.average_by_date())
fig.show()
