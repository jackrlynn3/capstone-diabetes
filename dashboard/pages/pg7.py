import dash
from dash import Dash, dcc, html, Input, Output
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
from dash import html, dcc
import pymssql

dash.register_page(__name__, name='DL Prediction')

layout = html.Div(
    [
        dbc.Row(
            [
                # Intro section
                dbc.Col(
                    [
                        dcc.Markdown('''
                            # Blood Glucose Levels Prediction using Deep Learning
                            Tracking blood glucose levels is essential to modern diabetes care. Deep learning time series models are used to predict blood glucose levels of Type-1 diabetes patients 30 minutes ahead. Additionally, patients are notified when their blood glucose levels exceed 300 mmol/L, which is considered dangerously high.
                        ''')
                    ],
                ),
                
                # Model introduction
                dbc.Col(
                    [
                        dcc.Markdown('''
                            ## Optimized Model
                            <Include description of model>
                        ''')
                    ],
                )
            ]
        ),

        # MODEL OPTIMIZATION
        dbc.Row(
            [
                # Header
                dbc.Row(
                    [
                        dcc.Markdown('''
                            ## Time Delay 
                            Time delays are varied by 5 minute intervals from 5 to 120 mins; this will determine how long in the future the model can successfully predict.
                        ''')
                    ]
                ),

                # Graphics
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Card(
                                    [
                                        dbc.CardImg(src="https://github.com/jackrlynn3/capstone-diabetes/blob/main/visualizations/deep-learning/time-delay-2.png?raw=true", top=True),
                                        dbc.CardBody(
                                            [
                                                dcc.Markdown('''
                                                    ### Evaluation of Time Delay Models
                                                    Time delays do not have any non-neglible effects on training time.
                                                ''')
                                            ]
                                        ),
                                    ],
                                    style={"width": "100%"}
                                )
                            ],
                            style={"flex-grow": "1"}
                        ),
                        
                        dbc.Col(
                            [
                                dbc.Card(
                                    [
                                        dbc.CardImg(src="https://raw.githubusercontent.com/jackrlynn3/capstone-diabetes/main/visualizations/deep-learning/time-delay-1.png?raw=true", top=True),
                                        dbc.CardBody(
                                            [
                                                dcc.Markdown('''
                                                    ### Comparison of Time Delay Models to Truth 
                                                    
                                                ''')
                                            ]
                                        ),
                                    ],
                                    style={"width": "100%"}
                                )
                            ],
                            style={"flex-grow": "2"}
                        )
                    ]
                )
            ]
        )
    ]
)