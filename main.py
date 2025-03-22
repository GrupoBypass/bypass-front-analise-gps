from modules import plot as plt, save as s
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=plt.plot_results_memory(s.get_results())
    ),

    dcc.Graph(
        id='example-graph',
        figure=plt.plot_results_memory_for_time(s.get_results())
    ),

    dcc.Graph(
        id='example-graph',
        figure=plt.plot_results_values(s.get_results())
    )
])

if __name__ == '__main__':
    app.run(debug=True)
