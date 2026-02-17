# -- 1: IMPORTS --
import plotly.express as px # it handles the actual chart creation
import pandas as pd # handles the data loading and organization
import numpy as np # handles numerical operations (if needed)
from dash import Dash, dcc, html, Input, Output # builds the web framework

# -- 2. Initialization & data -- 
# Create the Dash app instance
app = Dash(__name__)

# Load the data from your CSV file ( the file must be in the same folder as the project)
# df stands for "DataFrame" like a super powered Excell sheet in code
df = pd.read_csv("datavis_test.csv") 

# -- 3. The Layout ( the body) -- 
# This defines the visual structure of your dashboard using HTML-like componets
app.layout = html.Div([

    html.H2("Participant Data Dashboard"), # A Header 2 title
    
    html.Label("Viwe Hirerarchy By: "), # A simple text label

    # Dropdown component: This is our 'Input' device
    dcc.Dropdown( 
        id='hierarchy-dropdown',
        options=[
            # 'lable' is what the human sees in the menu
            # 'value' is the secret code sent to the computer (the key for our map)
            {'label': 'Country > Gender > Education', 'value': 'CGE'},
            {'label': 'Education > Country > Gender', 'value': 'ECG'},
            {'label': 'Gender > Education > Country', 'value': 'GEC'}
        ],
        value='CGE', # The default starting value
        clearable=False # Prevents the suer from deleting the selection
    ),

    # Graph component: A placeholder that will be filled by our callback function
    dcc.Graph(id='sunbrust-graph')

])

# -- 4. The Callback (the logic) -- 
# This section connects the Dropdown to the Graph.
# Whenever the 'value' of the 'hierarchy-dropdown' changes, this functon runs.
@app.callback(
    Output('sunbrust-graph', 'figure'), # the output target the graph's figure
    Input('hierarchy-dropdown','value') # the input trigger the dropdown's value
)

# Re-generating the sunbrust chart with the new hierarchy order
def update_hierarchy(selected_path):
    path_map = {
        'CGE': ['intv_BirthCount', 'intv_Gender', 'intv_Edu'],
        'ECG': ['intv_Edu', 'intv_BirthCount', 'intv_Gender'],
        'GEC': ['intv_Gender', 'intv_Edu', 'intv_BirthCount']
    }
    
    fig = px.sunburst(
        df, 
        path=path_map[selected_path], 
        values='intv_Age', # Slices sized by age
        color='intv_BirthCount',
        title=f"Hierarchy: {' -> '.join(path_map[selected_path])}"
    )
    
    fig.update_layout(margin=dict(t=40, l=0, r=0, b=0))
    return fig



if __name__ == '__main__':
    app.run(debug=True)