from re import X
import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import pymssql
from datetime import datetime as dt
# from config import server
# from config import database
# from config import username
# from config import password
# from config import table

dash.register_page(__name__, name='Personal Glucose Readings')

conn = pymssql.connect("gen10-data-fundamentals-22-05-sql-server.database.windows.net","haydenmuscha","P3ngu!ns87","group5database")

cursor = conn.cursor()

query = f'SELECT TOP(288) * FROM CGM_Stream WHERE PtID = 1 ORDER BY DeviceDtTM DESC;'
df = pd.read_sql(query, conn)

maxNdx = df['Glucose'].idxmax()
minNdx = df['Glucose'].idxmin()

maxGlu = df['Glucose'][maxNdx]
minGlu = df['Glucose'][minNdx]

maxdt = dt.strptime(df['DeviceDtTM'][maxNdx], '%m/%d/%Y, %H:%M:%S')
maxTime = maxdt.strftime("%I:%M %p")

mindt = dt.strptime(df['DeviceDtTM'][minNdx], '%m/%d/%Y, %H:%M:%S')
minTime = mindt.strftime("%I:%M %p")

df['Time'] = None

for x in df.index:
    a = dt.strptime(df['DeviceDtTM'][x], '%m/%d/%Y, %H:%M:%S')
    df['Time'][x] = a.strftime("%I:%M %p")

df['DeviceDtTM'] = df['DeviceDtTM'].astype('datetime64')

fig = go.Figure(go.Scatter(x=df['DeviceDtTM'], y=df['Glucose']))
fig.update_xaxes(title_text='Time')
fig.update_yaxes(title_text='Blood Glucose Level (mg/dL)')
fig.update_layout(
    xaxis = dict(
        tickmode = 'array',
        tickvals = [df['DeviceDtTM'][35],df['DeviceDtTM'][71],df['DeviceDtTM'][107],df['DeviceDtTM'][143],
        df['DeviceDtTM'][179],df['DeviceDtTM'][215],df['DeviceDtTM'][251]],
        ticktext = [df['Time'][35],df['Time'][71],df['Time'][107],df['Time'][143],
        df['Time'][179],df['Time'][215],df['Time'][251]]
    )
)

layout = html.Div(children=[
    html.H3(children='Blood Glucose Tracker'),

    html.Div(children='''
        Hello Jane, here are your updated blood glucose levels over the last 24 hours
    '''),

    dcc.Graph(
        id='Glucose-Readings-24hrs',
        figure=fig,
        animate=True
    ),

    dcc.Interval(
            id='graph-update',
            interval=5*1000,
            n_intervals=0
        ),

    html.P(id='max',
        children=[
            html.Span('Highest Blood Glucose Reading: '),
            html.Strong(f'{maxGlu}'),
            html.Span(f' mg/dL at {maxTime}')],
            style={'color':'#000000'}
        ),

    html.P(id='min',
        children=[
            html.Span('Lowest Blood Glucose Reading: '),
            html.Strong(f'{minGlu}'),
            html.Span(f' mg/dL at {minTime}')],
            style={'color':'#000000'}
        )
])

@callback(Output('Glucose-Readings-24hrs','figure'),[Input('graph-update','n_intervals')])

def update_graph(n):
    global query
    global df
    query = f'SELECT TOP(288) * FROM CGM_Stream WHERE PtID = 1 ORDER BY DeviceDtTM DESC;'
    df = pd.read_sql(query, conn)

    df['Time'] = None

    for x in df.index:
        a = dt.strptime(df['DeviceDtTM'][x], '%m/%d/%Y, %H:%M:%S')
        df['Time'][x] = a.strftime("%I:%M %p")

    df['DeviceDtTM'] = df['DeviceDtTM'].astype('datetime64')

    fig = go.Figure(go.Scatter(x=df['DeviceDtTM'], y=df['Glucose']))
    fig.update_xaxes(title_text='Time')
    fig.update_yaxes(title_text='Blood Glucose Level (mg/dL)')
    fig.update_layout(
        xaxis = dict(
            range=[min(df['DeviceDtTM']),max(df['DeviceDtTM'])],
            tickmode = 'array',
            tickvals = [df['DeviceDtTM'][35],df['DeviceDtTM'][71],df['DeviceDtTM'][107],df['DeviceDtTM'][143],
            df['DeviceDtTM'][179],df['DeviceDtTM'][215],df['DeviceDtTM'][251]],
            ticktext = [df['Time'][35],df['Time'][71],df['Time'][107],df['Time'][143],
            df['Time'][179],df['Time'][215],df['Time'][251]]
        ),
        yaxis = dict(range=[min(df['Glucose'])-10,max(df['Glucose']+10)])
    )

    return fig

@callback(Output('max','children'),[Input('graph-update','n_intervals')])

def update_max(n):
    maxNdx = df['Glucose'].idxmax()

    maxGlu = df['Glucose'][maxNdx]

    maxTmStr = dt.strftime(df['DeviceDtTM'][maxNdx], '%m/%d/%Y, %H:%M:%S')
    maxdt = dt.strptime(maxTmStr, '%m/%d/%Y, %H:%M:%S')
    maxTime = maxdt.strftime("%I:%M %p")

    return [html.Span('Highest Blood Glucose Reading: '),html.Strong(f'{maxGlu}'),html.Span(f' mg/dL at {maxTime}')]

@callback(Output('min','children'),[Input('graph-update','n_intervals')])

def update_max(n):
    minNdx = df['Glucose'].idxmin()

    minGlu = df['Glucose'][minNdx]

    minTmStr = dt.strftime(df['DeviceDtTM'][minNdx], '%m/%d/%Y, %H:%M:%S')
    mindt = dt.strptime(minTmStr, '%m/%d/%Y, %H:%M:%S')
    minTime = mindt.strftime("%I:%M %p")

    return [html.Span('Lowest Blood Glucose Reading: '),html.Strong(f'{minGlu}'),html.Span(f' mg/dL at {minTime}')]