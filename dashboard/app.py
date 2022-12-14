import dash
from dash import Dash, callback, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import matplotlib as mpl
# import gunicorn                     
from whitenoise import WhiteNoise  
import plotly.express as px
import urllib
import sqlalchemy as sa



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SPACELAB])
server = app.server



sidebar = dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
            ],
            vertical=True,
            pills=True,
            className="bg-light",
)

app.layout = dbc.Container([
    dbc.Row(dbc.Col(html.Div("Diabetes In USA: Public Health Led by Data",
        style={'fontSize':50, 'textAlign':'center', 'color':'#000000'}))
        ),

    dbc.Row(dbc.Col(html.Div("Group 5: Hayden Muscha, Jack Lynn, Samantha Wainright, Temesgen Fekadu",
        style={'fontSize':14, 'textAlign':'center', 'color':'#808080'}))
    ),

    html.Hr(),

    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    dash.page_container
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
], fluid=True)


if __name__ == "__main__":
    app.run(debug=False)