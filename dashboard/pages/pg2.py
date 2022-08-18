import dash
from dash import Dash, dcc, html, Input, Output
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
from dash import html, dcc
import pymssql
import pickle
from sklearn.metrics import  confusion_matrix, classification_report, roc_auc_score, auc, roc_curve
from sklearn.model_selection import train_test_split

dash.register_page(__name__, name='Predicting Diabetes')

# feature selection bar graph
try:
    selected_featuresDF = pd.read_csv('https://raw.githubusercontent.com/jackrlynn3/capstone-diabetes/main/models/machine-learning/models/sorted_features.csv')
except:
    selected_featuresDF = pd.read_csv('dashboard/assets/sorted_features.csv')
df = selected_featuresDF.sort_values(by='Anova_Score', ascending=True)
fig = px.bar(df, x='Anova_Score',y='Feature',title="Anova Score of Features",color_discrete_sequence=['Teal']*len(df))
fig.update_layout(title_x=0.5,
                yaxis_title=None,
                xaxis_title='Anova Score',
                width=500,
                height=700,
                bargap=0.05)


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
                    [
                    dcc.Graph(id='feature_selection',
                    figure=fig)
                    ], width = 6
                ),
                html.Div(html.Br())
            ],
        ),

        dbc.Row(
            [
                dbc.Col(
                    html.Img(src='https://raw.githubusercontent.com/jackrlynn3/capstone-diabetes/main/visualizations/machine-learning/LSVCConfusionMatrix.png')
                ),
                dbc.Col(
                    [
                    html.Img(src='https://raw.githubusercontent.com/jackrlynn3/capstone-diabetes/main/visualizations/machine-learning/ROCcurveLSVC.png')
                    ], width=6
                ),
            ],
        ),

    ]
)