import os
# ML libraries
import joblib
from joblib import load
import pickle
import pandas as pd

# Plotly and Dash libraries
import dash
from dash import Dash, dcc, html, Input, Output
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pymssql

# os.chdir('../..')
# home_path = os.getcwd()

# models_path = os.path.join(home_path,'models/machine-learning/models')
# models_path

#anova selected features
selected_featuresDF = pd.read_csv('https://raw.githubusercontent.com/jackrlynn3/capstone-diabetes/main/models/machine-learning/models/sorted_features.csv')
df = selected_featuresDF.sort_values(by='Anova_Score', ascending=True)
fig = px.bar(df, x='Anova_Score',y='Feature')
fig.update_layout(title="Anova Score of Features",
                yaxis_title=None)

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
                    html.Img(src='https://raw.githubusercontent.com/jackrlynn3/capstone-diabetes/main/visualizations/machine-learning/ROC_AUC_LSVC.png')
                    ], width=4
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

# @ callback(
#     Output(component_id='selected_features',
#     component_property='figure'),
#     [Input(component_id)]
    
#     )

                # dbc.Col(
                #     [
                #     dcc.Graph(
                #         id='selected_features',
                #         figure=fig),
                #     ], width=4
                # ),
