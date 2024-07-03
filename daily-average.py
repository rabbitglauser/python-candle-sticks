import plotly.graph_objects as go
import pandas as pd

# Load the dataset from a public URL
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

# Calculate the 20-day and 100-day moving averages of the closing stock prices
df['20_day_ma'] = df['AAPL.Close'].rolling(window=20).mean()
df['100_day_ma'] = df['AAPL.Close'].rolling(window=100).mean()

# Convert the date column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Create a 3D Scatter plot
fig = go.Figure()

# Add the 3D scatter plot for the closing prices
fig.add_trace(go.Scatter3d(
    x=df['Date'],
    y=df['AAPL.Close'],
    z=df['20_day_ma'],
    mode='markers',
    marker=dict(
        size=5,
        color=df['AAPL.Close'],                # set color to the closing prices
        colorscale='Viridis',   # choose a colorscale
        opacity=0.8
    ),
    name='AAPL Close'
))

# Add the 3D line plot for the 20-day moving average
fig.add_trace(go.Scatter3d(
    x=df['Date'],
    y=df['AAPL.Close'],
    z=df['20_day_ma'],
    mode='lines',
    line=dict(
        color='blue',
        width=2
    ),
    name='20 Day MA'
))

# Add the 3D line plot for the 100-day moving average
fig.add_trace(go.Scatter3d(
    x=df['Date'],
    y=df['AAPL.Close'],
    z=df['100_day_ma'],
    mode='lines',
    line=dict(
        color='red',
        width=2
    ),
    name='100 Day MA'
))

# Update layout
fig.update_layout(
    title='3D Visualization of AAPL Stock Prices with Moving Averages',
    scene=dict(
        xaxis_title='Date',
        yaxis_title='AAPL Close Price',
        zaxis_title='20 Day MA',
        xaxis=dict(type='date')
    )
)

# Display the chart
fig.show()
