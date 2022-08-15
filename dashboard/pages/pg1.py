import dash
from dash import Dash, dcc, html, Input, Output
dash.register_page(__name__, path='/', name='Home') # '/' is home page
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import pymssql

conn = pymssql.connect("gen10-data-fundamentals-22-05-sql-server.database.windows.net","haydenmuscha","P3ngu!ns87","group5database")

query = f'SELECT * FROM CensusStat'
df1 = pd.read_sql(query, conn)

query2 = f'SELECT * FROM Demographic'
df2 = pd.read_sql(query2, conn)

query3 = f'SELECT * FROM Metric'
df3 = pd.read_sql(query3, conn)

merg1 = pd.merge(df1, df2, how="inner", on="demoID")
merg2 = pd.merge(merg1, df3, how="inner", on="metricID")

merg2.rename(columns = {'value':'percent'}, inplace = True)

diamap = merg2.loc[merg2['demo_group'] == 'General']
diamap = diamap.loc[diamap['metric'] == 'diabetes']
diamap = diamap[["year", "stateID", "percent"]]

linemap = diamap

diamap = diamap[diamap.stateID != 'DC']
diamap = diamap[diamap.stateID != 'US']


layout = html.Div(
    [
        dbc.Row(
            [
                dcc.Markdown('''
                    Textarea content initialized ghpajsiv ynsl;athnvu9reayhtfgr08iweweweweweweweweweweweweweweweweweweweweqa['dhfir[aqIHSRUIOEP;]]
                    
                    with multiple lines of text
                    
                    what is to be put here is to be decided
                ''')
            ],
        ),  
        dbc.Row(
            [
                dbc.Col(html.H1("Diabetes by State from 2011 - 2020",
                    className='text-center text-primary mb-4'),
                ),
                dbc.Col(html.H1("Diabetes Over Time from 2011 - 2020 by Location",
                    className='text-center text-primary mb-4'),
                )
            ],
        ),        
        dbc.Row(
            [
                dbc.Col(
                    [
                    dcc.Slider(id="slct_year", value = 2011, min = 2011, max = 2020, step= None,
                                     marks = {
                                        2011: '2011',
                                        2012: '2012',
                                        2013: '2013',
                                        2014: '2014',
                                        2015: '2015',
                                        2016: '2016',
                                        2017: '2017',
                                        2018: '2018',
                                        2019: '2019',
                                        2020: '2020',
                                        }
                                        )
                    ]
                ),
                dbc.Col(
                dcc.Dropdown(id="slct_state", options =[{'label':x, 'value':x} for x in linemap.sort_values('stateID')['stateID'].unique()],
                        value='US')
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                    dcc.Graph(id='diabetes_map', figure={}),
                    ], width=6
                ),
                dbc.Col(
                    [
                    dcc.Graph(id='diabetes_line'),
                    ], width=6
                )
            ]
        ),
        dbc.Row(
            [
                dcc.Markdown('''
                    Sources
                    
                    with multiple lines of text
                    
                    what is to be put here is to be decided
                ''')
            ],
        ),
    ]
)


@callback(
     Output(component_id='diabetes_map', component_property='figure'),
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):



    dff = diamap.copy()
    dff = dff[dff["year"] == option_slctd]


    # Plotly Express
    fig = px.choropleth(
        data_frame=dff,
        locationmode='USA-states',
        locations='stateID',
        scope="usa",
        color='percent',
        hover_data=['stateID', 'percent'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        range_color=(0,16),
        labels={'stateID': 'percent'},
        template='plotly_dark'
    )
    return fig
@callback(
     Output(component_id='diabetes_line', component_property='figure'),
    [Input(component_id='slct_state', component_property='value')]
)
def build_graph(state_slctd):
    df = linemap[(linemap['stateID']==state_slctd)]
    df = df.sort_values(by='year')
    figln = px.line(df, x='year', y='percent')
    return figln