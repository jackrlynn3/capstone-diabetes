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
                dcc.Markdown('''##### The Growth of Diabetes in the USA''')
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Markdown('''
                    Diabetes has the seventh largest disease burden in the United States and continues to
                    grow year by year. In 2020, 10.6% of the population were living with diabetes, which is
                    a 12% increase from 2011. Based on the heat map below we can see that the states most
                    affected by diabetes are West Virginia, Alabama, and Mississippi.
                    ''')
                ),
                dbc.Col(dcc.Markdown('''
                    Like most non-communicable diseases, diabetes differentially affects people based on
                    genetic, community, and lifestyle factors that potentiate the development of diabetes.
                    In the next page we will take a deeper look into these factors.
                    ''')
                ),
                html.Div(html.Br())
            ],
        ),
        dbc.Row(
            [
                dcc.Markdown(''' \n ''')
            ]

        ),
        dbc.Row(
            [
                dbc.Col(html.H3("Diabetes by State from 2011 - 2020",
                    className='text-left text-primary mb-4'),
                ),
                dbc.Col(html.H3("Diabetes Over Time from 2011 - 2020 by Location",
                    className='text-left text-primary mb-4'),
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
                html.Div([html.Br(),html.Br()]),
                dcc.Markdown('''##### Sources'''),
                dbc.Col([html.Div('''
                            Centers for Disease Control and Prevention. (2017, January 26). National Health and Nutrition Examination
                            Survey. Retrieved August 5, 2022, from www.kaggle.com website: 
                            https://www.kaggle.com/datasets/cdc/national-health-and-nutrition-examination-survey
                            '''),
                        html.Br(),
                        html.Div('''
                            Centers for Disease Control and Prevention. (2022, March 24). U.S. Chronic Disease Indicators: Diabetes | 
                            Chronic Disease and Health Promotion Data & Indicators. Retrieved August 5, 2022, from Socrata 
                            website: https://chronicdata.cdc.gov/Chronic-Disease-Indicators/U-S-Chronic-Disease-Indicators-Diabetes/f8ti-h92k/data
                            '''),
                        html.Br(),
                        html.Div('''
                            JAEB Center for Health Research. (2019). A Randomized Clinical Trial to Assess the Efficacy and Safety of 
                            Continuous Glucose Monitoring in Youth < 8 with Type 1 Diabetes. Retrieved August 5, 2022, from 
                            public.jaeb.org website: https://public.jaeb.org/dataset/563
                        '''),
                        html.Br(),
                        html.Div('''
                            United States Census Bureau. (2022a, March 17). American Community Survey: B06009: PLACE OF BIRTH BY 
                            EDUCATIONAL ATTAINMENT IN THE UNITED STATES. Retrieved August 5, 2022, from data.census.gov 
                            website: 
                            https://data.census.gov/cedsci/table?q=education%20by%20state&tid=ACSDT5Y2020.B06009
                        ''')
                        ]),
                dbc.Col([html.Div('''
                            Centers for Disease Control and Prevention. (2021, June 3). National Center for Chronic Disease Prevention 
                            and Health Promotion, Division of Nutrition, Physical Activity, and Obesity. Data, Trend and Maps 
                            [online]. Retrieved August 5, 2022, from Cdc.gov website: https://www.cdc.gov/nccdphp/dnpao/data-trends-maps/index.html
                            '''),
                        html.Br(),
                        html.Div('''
                            Chen, Y., Zhang, X.-P., Yuan, J., Cai, B., Wang, X.-L., Wu, X.-L., … Li, X.-Y. (2018, August 21). Data from: 
                            Association of body mass index and age with incident diabetes in Chinese adults: a population-based 
                            cohort study. Retrieved August 5, 2022, from datadryad.org website: 
                            https://doi.org/10.5061/dryad.ft8750v
                        '''),
                        html.Br(),
                        html.Div('''
                            U.S. Department of Agriculture. (2021, September 8). Food Security in the U.S. USDA (2019). Retrieved from 
                            www.ers.usda.gov website: https://www.ers.usda.gov/topics/food-nutrition-assistance/food-security-in-the-u-s/interactive-charts-and-highlights/
                        '''),
                        html.Br(),
                        html.Div('''
                            United States Census Bureau. (2022b, March 17). American Community Survey: S1901: INCOME IN THE PAST 
                            12 MONTHS (IN 2020 INFLATION-ADJUSTED DOLLARS) U.S. Census Bureau (2020). Retrieved from 
                            data.census.gov website: https://data.census.gov/cedsci/table?q=S1901&tid=ACSST5Y2020.S1901
                        ''')
                        ])
            ]
        )
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
        color_continuous_scale=['#FFFF8F','#C41E3A'],
        range_color=(0,16),
        labels={"stateID": "State",
                'percent': "Percent of Population"
        }
    )
    return fig
@callback(
     Output(component_id='diabetes_line', component_property='figure'),
    [Input(component_id='slct_state', component_property='value')]
)
def build_graph(state_slctd):
    df = linemap[(linemap['stateID']==state_slctd)]
    df = df.sort_values(by='year')
    figln = px.line(df, x='year', y='percent',
            labels={
                "year": "Year",
                "percent": "Percent of Population"

            })
    return figln