import pandas as pd
import plotly.graph_objects as go
import os

# Path to the Excel file
file_path = '~/myproject/testdata.xlsx'

# Read data from Excel
df = pd.read_excel(file_path)

# Set the 'Timestamp' column as the index
df.set_index('Timestamp', inplace=True)

# Get all sensor columns to be visualized
sensor_columns = df.columns

# Create a figure for the animation
fig = go.Figure()

# Create frames for animation for each timestamp
frames = []

for i in range(1, len(df)):
    frame_data = []
    for sensor in sensor_columns:
        frame_data.append(go.Scatter(
            x=df.index[:i],  # X-axis: Timestamp
            y=df[sensor][:i],  # Y-axis: Sensor temperature
            mode='lines',
            name=sensor
        ))
    
    frames.append(go.Frame(data=frame_data, name=str(i)))

# Add frames to the figure
fig.frames = frames

# Add initial traces for each sensor
for sensor in sensor_columns:
    fig.add_trace(go.Scatter(
        x=df.index, 
        y=df[sensor], 
        mode='lines',
        name=sensor
    ))

# Set up the layout for animation controls
fig.update_layout(
    updatemenus=[{
        'buttons': [
            {
                'args': [None, {'frame': {'duration': 50, 'redraw': True}, 'fromcurrent': True, 'mode': 'immediate'}],
                'label': 'Play',  # Button to play the animation
                'method': 'animate'
            },
            {
                'args': [[None], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'immediate'}],
                'label': 'Pause',  # Button to pause the animation
                'method': 'animate'
            }
        ],
        'type': 'buttons',
        'showactive': False  # Do not show active button
    }]
)

# Path to save the HTML file
html_file_path = os.path.join(os.path.expanduser("~"), 'myproject/animasi_juniper_graph.html')

# Save the animation figure to an HTML file
fig.write_html(html_file_path)

# Display confirmation message
print(f"Animation successfully saved to '{html_file_path}'")
