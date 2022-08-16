import dash
from dash import Dash, dcc, html, Input, Output
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
from dash import html, dcc
import pymssql
dash.register_page(__name__, name='Predicting Diabetes')

layout = html.Div(
    [
        dbc.Row(
            [
                dcc.Markdown('''##### Can We Predict Diabetes''')
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Markdown('''
                    Explain the Model
                    things
                    stuff
                    ''')
                ),
                dbc.Col(
                    html.Img(src='https://raw.githubusercontent.com/jackrlynn3/capstone-diabetes/main/visualizations/machine-learning/CM_Tuned_SF_LSVC.png')
                ),
                dbc.Col(
                    html.Img(src='https://raw.githubusercontent.com/jackrlynn3/capstone-diabetes/main/visualizations/machine-learning/CM_Tuned_SF_SVC.png')
                ),
                html.Div(html.Br())
            ],
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                    (html.Img(
                        src=('https://raw.githubusercontent.com/jackrlynn3/capstone-diabetes/main/visualizations/machine-learning/SF_anova_scores.png'),
                        style={
                            'width':'10%',
                            'height':'10%'
                            }
                            )
                    )
                    ],
                ),
                dbc.Col(
                    [
                    html.Img(src='https://raw.githubusercontent.com/jackrlynn3/capstone-diabetes/main/visualizations/machine-learning/ROC_AUC_LSVC.png')
                    ], width=6
                ),
            ],
        ),
    ]
)