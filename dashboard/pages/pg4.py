import dash
from dash import Dash, dcc, html, Input, Output
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
from dash import html, dcc
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


incomestates = merg2.loc[merg2['category'] == 'income bracket']
incomestates = incomestates[["stateID", "percent","demo_group"]]
incomestates.rename(columns = {'demo_group':'income bracket'}, inplace = True)

foodstates = merg2.loc[merg2['metric'] == 'food security']
foodstates = foodstates[["year","stateID", "percent","demo_group"]]
foodstates = foodstates[["year","stateID", "percent"]]
foodstates = foodstates[foodstates.stateID != 'DC']
foodstates = foodstates[foodstates.stateID != 'US']


edustates = merg2.loc[merg2['category'] == 'education level']
edustates = edustates[["stateID", "percent","demo_group"]]
edustates.rename(columns = {'demo_group':'education'}, inplace = True)
edustates['education'] = edustates['education'].replace(['Bachelors Degreee',],['Bachelors Degree',])

dash.register_page(__name__, name='National Examination')

layout = html.Div(
    [
        dbc.Row(
            [
                dcc.Markdown('''#### Lifestyle Factors ''')
            ],
        ),
        dbc.Row(
            [
                dcc.Markdown('''

                Based on what we see from the NHANES data, we wanted to look at how these general lifestyle aspects played out across the U.S. on a State-by-State Level. Frequency of eating out is represented as Food Insecurity (the state of being without reliable access to a sufficient quantity of affordable, nutritious food).

                ''')
            ],
        ),  
        dbc.Row(
            [
                dbc.Col(html.H4("Income Brackets By Percentage of Population by State",
                    className='text-center text-primary mb-4'),
                ),
                dbc.Col(html.H4("Educational Attainment By Percentage of Population by State",
                    className='text-center text-primary mb-4'),
                ),
                dbc.Col(html.H4("Food Insecurity By Percentage of Population by State by Year",
                    className='text-center text-primary mb-4'),
                )
            ],
        ),
        dbc.Row(
            [
                dbc.Col(
                dcc.Dropdown(id="slct_state1", 
                options=[
                     {'label': 'Less than 10,000', 'value': 'Less than 10,000'},
                     {'label': '10,000 to 14,999', 'value': '10,000 to 14,999'},
                     {'label': '15,000 to 24,999', 'value': '15,000 to 24,999'},
                     {'label': '25,000 to 34,999', 'value': '25,000 to 34,999'},
                     {'label': '35,000 to 49,999', 'value': '35,000 to 49,999'},
                     {'label': '50,000 to 74,999', 'value': '50,000 to 74,999'},
                     {'label': '75,000 to 99,999', 'value': '75,000 to 99,999'},
                     {'label': '100,000 to 149,999', 'value': '100,000 to 149,999'},
                     {'label': '150,000 to 199,999', 'value': '150,000 to 199,999'},
                     {'label': '200,000 or more', 'value': '200,000 or more'},
                ],
                        value='Less than 10,000'),width=4
                ),
                dbc.Col(
                dcc.Dropdown(id="slct_state2",
                options=[
                     {'label': 'Less than high school graduate', 'value': 'Less than high school graduate'},
                     {'label': 'High school graduate (includes equivalency)', 'value': 'High school graduate (includes equivalency)'},
                     {'label': 'Some college or associate degree', 'value': 'Some college or associate degree'},
                     {'label': 'Bachelors Degree', 'value': 'Bachelors Degree'},
                ],
                        value='Less than high school graduate'), width= 4
                ),
                dbc.Col(
                dcc.Dropdown(id="slct_state3", options =[{'label':x, 'value':x} for x in foodstates.sort_values('year')['year'].unique()],
                        value=2003), width= 4
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                    dcc.Graph(id='income_map', figure={}),
                    ], width=4
                ),
                dbc.Col(
                    [
                    dcc.Graph(id='education_map', figure={}),
                    ], width=4
                ),
                dbc.Col(
                    [
                    dcc.Graph(id='food_map', figure={}),
                    ], width=4
                ),
            ]
        ),
        dbc.Row(
            [
                dcc.Markdown('''#### Call to action:'''),
                dcc.Markdown('''

                The maps that infer the closets similarity with both the Diabetes Distribution in the U.S. and the Indicators from the NHANES are Educational Attainment, and Food Insecurity. 
                From this we would recommend a stronger push in these regions (primarily the southeast), to increase the availability of nutritious affordable food in these areas. 
                Alongside this, a national push for greater educational attainment to help spur greater income in these regions as well.

                ''')
            ],
        ),
    ]
)
@callback(
     Output(component_id='income_map', component_property='figure'),
    [Input(component_id='slct_state1', component_property='value')]
)
def update_graph(option_slctd):



    dff = incomestates.copy()
    dff = dff[dff["income bracket"] == option_slctd]


    # Plotly Express
    fig = px.choropleth(
        data_frame=dff,
        locationmode='USA-states',
        locations='stateID',
        scope="usa",
        color='percent',
        hover_data=['stateID', 'percent'],
        color_continuous_scale=['#FFFF8F','#C41E3A'],
        range_color=(0,25),
        labels={"stateID": "State",
                'percent': "Percent"
        }
    )
    return fig

@callback(
     Output(component_id='education_map', component_property='figure'),
    [Input(component_id='slct_state2', component_property='value')]
)    
def update_graph(option_slctd2):



    df = edustates.copy()
    df = df[df["education"] == option_slctd2]


    # Plotly Express
    fig2 = px.choropleth(
        data_frame=df,
        locationmode='USA-states',
        locations='stateID',
        scope="usa",
        color='percent',
        hover_data=['stateID', 'percent'],
        color_continuous_scale=['#FFFF8F','#C41E3A'],
        range_color=(0,40),
        labels={"stateID": "State",
                'percent': "Percent"
        }
    )
    return fig2
@callback(
     Output(component_id='food_map', component_property='figure'),
    [Input(component_id='slct_state3', component_property='value')]
)    
def update_graph(option_slctd3):



    d = foodstates.copy()
    d = d[d["year"] == option_slctd3]


    # Plotly Express
    fig3 = px.choropleth(
        data_frame=d,
        locationmode='USA-states',
        locations='stateID',
        scope="usa",
        color='percent',
        hover_data=['stateID', 'percent'],
        color_continuous_scale=['#FFFF8F','#C41E3A'],
        range_color=(0,20),
        labels={"stateID": "State",
                'percent': "Percent"
        }
    )
    return fig3
