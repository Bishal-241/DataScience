'''import plotly.graph_objects as go

# Data for the bar graph
categories = ['Category A', 'Category B', 'Category C']
values = [10, 15, 7]

# Create the bar graph with green bars
fig = go.Figure(data=[go.Bar(x=categories, y=values, marker_color='green')])

# Add title and labels
fig.update_layout(
    title='Basic Bar Graph',
    xaxis_title='Categories',
    yaxis_title='Values'
)

# Show the graph
fig.show() '''


import plotly.express as px
import pandas as pd

# Sample data: Replace this with your actual dataset
data = {
    'Age': [22, 25, 23, 30, 28, 22, 24, 26, 29, 25, 27, 30, 22, 23, 24, 25, 26, 27, 28, 29]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a histogram using Plotly
fig = px.histogram(
    df, 
    x='Age', 
    nbins=10,  # Number of bins for the histogram
    title='Class Age Distribution',  # Title of the graph
    labels={'Age': 'Age (years)'},  # Label for the x-axis
    opacity=0.7,  # Adjust the opacity of the bars
    color_discrete_sequence=['#1f77b4']  # Custom color for the bars
)

# Update layout for better visualization
fig.update_layout(
    xaxis_title='Age (years)',  # X-axis label
    yaxis_title='Number of Students',  # Y-axis label
    bargap=0.1,  # Gap between bars
    template='plotly_white'  # Use a clean white template
)

# Show the plot
fig.show()


