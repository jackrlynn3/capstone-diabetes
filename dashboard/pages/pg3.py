import dash
from dash import Dash, dcc, html, Input, Output
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
from dash import html, dcc
import pymssql
conn = pymssql.connect("gen10-data-fundamentals-22-05-sql-server.database.windows.net","haydenmuscha","P3ngu!ns87","group5database")
dash.register_page(__name__, name='Indicators and Factors')

layout = html.Div(
    [
        dbc.Row(
            [
                dcc.Markdown('# Indicators and factors of Diabetes Type 2')
            ],
        ),
        dbc.Row(
            [
                dcc.Markdown('''
                    Indicators of Diabetes Type 2
                    
                    with multiple lines of text
                    
                    what is to be put here is to be decided
                ''')
            ],
        ),
        dbc.Row(
            [
            dbc.Col(
                dcc.Dropdown(id="slct_state1", options =[{'label':x, 'value':x} for x in incomestates.sort_values('income bracket')['income bracket'].unique()],
                        value='Less than 10,000')
                ),
            ],
        ),
        
    ]
)