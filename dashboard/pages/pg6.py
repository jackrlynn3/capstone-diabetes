import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import pymssql
# from config import server
# from config import database
# from config import username
# from config import password
# from config import table

dash.register_page(__name__, name='Personal Glucose Readings')

conn = pymssql.connect(server,username,password,database)

cursor = conn.cursor()

query = f'SELECT TOP(288) * FROM {table} WHERE PtID = 1 ORDER BY DeviceDtTM DESC;'
df = pd.read_sql(query, conn)

maxNdx = df['Glucose'].idxmax()
minNdx = df['Glucose'].idxmin()

maxGlu = df['Glucose'][maxNdx]
minGlu = df['Glucose'][minNdx]

maxTmstmpStr = df['DeviceDtTM'][maxNdx]
minTmstmpStr = df['DeviceDtTM'][minNdx]

maxTmstmp = maxTmstmpStr.split(', ')
minTmstmp = minTmstmpStr.split(', ')

maxTm = maxTmstmp[1].split(':')
minTm = minTmstmp[1].split(':')

maxTime = maxTm[0] + ':' + maxTm[1]
minTime = minTm[0] + ':' + minTm[1]

maxDt = maxTmstmp[0].split('/2000')
minDt = minTmstmp[0].split('/2000')

df['DeviceDtTM'] = df['DeviceDtTM'].astype('datetime64')

lineChart = df[['DeviceDtTM','Glucose']]

fig = px.line(lineChart, x='DeviceDtTM', y='Glucose', title='24-Hour Glucose Readings')

layout = html.Div(children=[
    html.H1(children='Glucose Tracker'),

    html.Div(children='''
        Hello [name], here are your updated glucose levels over the last 24 hours
    '''),

    dcc.Graph(
        id='Glucose-Readings-24hrs',
        figure = fig
    ),

    html.H3(children=f'''
        Highest Glucose Reading is {maxGlu} at {maxTime}
    '''),

    html.H3(children=f'''
        Lowest Glucose Reading is {minGlu} at {minTime}
    ''')
])
