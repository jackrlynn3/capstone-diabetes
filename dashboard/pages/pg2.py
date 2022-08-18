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
fig = px.bar(df, x='Anova_Score',y='Feature',title="Predictive Features",color_discrete_sequence=['Teal']*len(df))
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
                dcc.Markdown('''##### Can We Predict Diabetes?''')
            ]
        ),

        dbc.Row(
            [
                dbc.Col(dcc.Markdown('''
                        The ability to predict a Type-2 diabetes diagnosis can be done with machine learning.
                        Type 2 diabetes is mainly lifestyle related and develops overtime. When using an ANOVA F-test, on the Chen et al. data we see that the strongest predictive features are age, bmi, blood pressure, and cholesterol.

                        And ROC Curve and confusion matrix represent the performance of the LinearSVC algorithm, as well as it's ability to correctly predict diabetes. 

                    ''')
                ),
            ],
        ),

        dbc.Row(
            [
                dbc.Col(
                    [
                    dcc.Graph(id='feature_selection',
                    figure=fig)
                    ], width=4
                ),
                dbc.Col(
                    [
                    html.Img(src='https://raw.githubusercontent.com/jackrlynn3/capstone-diabetes/main/visualizations/machine-learning/LSVCConfusionMatrix.png')
                    ], width=4
                ),
                dbc.Col(
                    [
                    html.Img(src='https://raw.githubusercontent.com/jackrlynn3/capstone-diabetes/main/visualizations/machine-learning/ROCcurveLSVC.png')
                    ], width=4
                ),
                html.Div(html.Br())
            ],
        ),

    ]
)