# imports
# dash
import dash
from dash import Dash, dcc, html, Input, Output
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
# data processing
import pandas as pd
from dash import html, dcc
import pymssql
# model and performance
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import train_test_split, cross_val_score, RepeatedStratifiedKFold


dash.register_page(__name__, name='Predicting Diabetes')

# load data
df = pd.read_csv('https://raw.githubusercontent.com/jackrlynn3/capstone-diabetes/main/etl/chinese_medical/data_standardized.csv')
df = df.drop(["Unnamed:0"],axis=1)

# split into test and train
def split_data(df):
    # retrieve array
    dataset = df.values
    # split into input and output
    X = dataset[:, :-1]
    y = dataset[:,-1]
    # split into test and train sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, stratify=df['diabetes'],random_state=1)
    
    return (X_train,X_test,y_train,y_test)

# feature selection
def anova_select_features(X_train, y_train, X_test):
    # configure to select all features
    afs = SelectKBest(score_func=f_classif, k='all')
    # learn relationship from training data
    afs.fit(X_train, y_train)
    # transform train and test input data
    X_train_fs = afs.transform(X_train)
    X_test_fs = afs.transform(X_test)
    
    return X_train_fs, X_test_fs, afs

#############################################################
####################### PAGE LAYOUT #########################
layout = html.Div(
    [

        dbc.Row([
                dcc.Markdown('''## Can We Predict Diabetes''')
            ]),

        dbc.Row([
                dbc.Col(dcc.Markdown('''
                    Explain the Model

                    things

                    stuff!!
                    ''')),

                dbc.Col(
                    html.Img(src='https://raw.githubusercontent.com/jackrlynn3/capstone-diabetes/main/visualizations/machine-learning/CM_Tuned_SF_LSVC.png')),

                dbc.Col(
                    html.Img(src='https://raw.githubusercontent.com/jackrlynn3/capstone-diabetes/main/visualizations/machine-learning/CM_Tuned_SF_SVC.png')),

                html.Div(html.Br())
            ],),

        dbc.Row([
                dbc.Col([
                    (html.Img(
                        src=('https://raw.githubusercontent.com/jackrlynn3/capstone-diabetes/main/visualizations/machine-learning/SF_anova_scores.png'),)
                    )
                    ],width=6),

                dbc.Col(
                    [
                    html.Img(src='https://raw.githubusercontent.com/jackrlynn3/capstone-diabetes/main/visualizations/machine-learning/ROC_AUC_LSVC.png')
                    ], width=6),
            ],),
    ]
)