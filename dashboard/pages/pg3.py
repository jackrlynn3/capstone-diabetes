import dash
from dash import Dash, dcc, html, Input, Output
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
from dash import html, dcc
import pymssql
import numpy as np
conn = pymssql.connect("gen10-data-fundamentals-22-05-sql-server.database.windows.net","haydenmuscha","P3ngu!ns87","group5database")

query = f'SELECT * FROM NHAINESStat'
df1 = pd.read_sql(query, conn)

query = f'SELECT * FROM Demographic'
df2 = pd.read_sql(query, conn)

df3 =pd.merge(df1, df2, how='left', left_on=['educationID'], right_on=['demoID'])
df3 = df3.rename(columns={"demo_group": "Education"})
df3 =df3.drop(['demoID','educationID','category'], axis=1)

df4 =pd.merge(df3, df2, how='left', left_on=['smokerID'], right_on=['demoID'])
df4['demo_group'] = df4['demo_group'].fillna('no info')
df4 = df4.rename(columns={"demo_group": "smokingstatus"})
df4 =df4.drop(['demoID','smokerID','category'], axis=1)

df5 =pd.merge(df4, df2, how='left', left_on=['drinkerID'], right_on=['demoID'])
df5['demo_group'] = df5['demo_group'].fillna('no info')

df5 = df5.rename(columns={"demo_group": "drinkkingstatus"})
df5 =df5.drop(['demoID','drinkerID','category'], axis=1)

df6 =pd.merge(df5, df2, how='left', left_on=['incomeID'], right_on=['demoID'])
df6['demo_group'] = df6['demo_group'].fillna('no info')
df6 = df6.rename(columns={"demo_group": "income"})
df6 =df6.drop(['demoID','incomeID','category'], axis=1)
df6[['diabetes', 'prediabetes', 'diabetesRisk']] = df6[['diabetes', 'prediabetes', 'diabetesRisk']].fillna(value="False")
df6['diabetes'] = df6['diabetes'].astype("string")
df6['prediabetes'] = df6['prediabetes'].astype("string")
df6['diabetesRisk'] = df6['diabetesRisk'].astype("string")
df6["diabetes"] = np.where(df6["diabetes"] == "True", 1, 0)
df6["prediabetes"] = np.where(df6["prediabetes"] == "True", 1, 0)
df6["diabetesRisk"] = np.where(df6["diabetesRisk"] == "True", 1, 0)
df6['diabetes'] = df6['diabetes'].astype("int")
df6['prediabetes'] = df6['prediabetes'].astype("int")
df6['diabetesRisk'] = df6['diabetesRisk'].astype("int")

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
                
                ),
            ],
        ),
        
    ]
)