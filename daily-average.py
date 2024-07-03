# Import necessary libraries
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset from a public URL
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

# Calculate the 20-day and 100-day moving averages of the closing stock prices
df['20_day_ma'] = df['AAPL.Close'].rolling(window=20).mean()
df['100_day_ma'] = df['AAPL.Close'].rolling(window=100).mean()

# Create a Candlestick chart with date as x-axis and various stock prices as y-axis
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['AAPL.Open'], high=df['AAPL.High'],
                                     low=df['AAPL.Low'], close=df['AAPL.Close'])
                      ])

# Add traces of 20-day and 100-day moving averages to the chart
fig.add_trace(go.Scatter(x=df['Date'], y=df['20_day_ma'], mode='lines', name='20 Day MA'))
fig.add_trace(go.Scatter(x=df['Date'], y=df['100_day_ma'], mode='lines', name='100 Day MA'))

# Update the layout of the chart
fig.update_layout(
    title='The Great Recession',  # Title of the chart
    yaxis_title='AAPL Stock',  # Y-axis title
    shapes=[dict(
        x0='2016-12-09', x1='2016-12-09', y0=0, y1=1, xref='x', yref='paper',
        line_width=2)],  # Drawing a vertical line at '2016-12-09'
    annotations=[dict(
        x='2016-12-09', y=0.05, xref='x', yref='paper',
        showarrow=False, xanchor='left', text='Increase Period Begins')]  # Adding an annotation at '2016-12-09'
)

# Display the chart
fig.show()
