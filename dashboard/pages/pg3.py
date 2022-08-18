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

conditions = [
    (df6['bmi'] < 18.5),
    (df6['bmi'] >= 18.5) & (df6['bmi'] < 25),
    (df6['bmi'] >= 25) & (df6['bmi'] < 30),
    (df6['bmi'] >= 30)
]

values = ['underweight', 'normal', 'overweight', 'obese']

df6['bmicategory'] = np.select(conditions, values)

conditions = [
    (df6['mealsAtHome'] < 1),
    (df6['mealsAtHome'] >= 1) & (df6['mealsAtHome'] < 2),
    (df6['mealsAtHome'] >= 2) & (df6['mealsAtHome'] < 5),
    (df6['mealsAtHome'] >= 5) & (df6['mealsAtHome'] < 8),
    (df6['mealsAtHome'] >= 8)
]

values = ['Never', 'Once a week', 'Every other day', 'Daily','More than once a day']

df6['eatingout'] = np.select(conditions, values)

education = df6[['diabetes','prediabetes','diabetesRisk','Education']]
education['Education'] = education['Education'].replace(['Some College or Associates degree','No High School Diploma or GED','High School Diploma or GED/equivalent'],['Some College','No HS Diploma/GED','HS Diploma/GED'])

bmidist = df6[['diabetes','prediabetes','diabetesRisk','bmicategory']]

foodchoice = df6[['diabetes','prediabetes','diabetesRisk','eatingout']]

income = df6[['diabetes','prediabetes','diabetesRisk','income']]

dash.register_page(__name__, name='Indicators and Factors')

fig1 = px.histogram(education, x="Education", y=['diabetes','prediabetes','diabetesRisk'],
                    barmode='group',
                    histfunc='sum',
                    labels=dict(x="Education", y="Number of Responses"))
fig1.update_layout(xaxis={'categoryorder':'array', 'categoryarray':['Unknown','No HS Diploma/GED','HS Diploma/GED','Some College', 'Bachelors or Higher']},)
fig1.update_yaxes(title_text='Number of Those Surveyed')
fig1.update_xaxes(title_text='Education')

fig2 = px.histogram(bmidist, x="bmicategory", y=['diabetes','prediabetes','diabetesRisk'],
                    barmode='group',
                    histfunc='sum',)
fig2.update_layout(xaxis={'categoryorder':'array', 'categoryarray':['underweight','normal','overweight','obese']},)
fig2.update_yaxes(title_text='Number of Those Surveyed')
fig2.update_xaxes(title_text='BMI Categories')

fig3 = px.histogram(foodchoice, x="eatingout", y=['diabetes','prediabetes','diabetesRisk'],
                    barmode='group',
                    histfunc='sum',)
fig3.update_layout(xaxis={'categoryorder':'array', 'categoryarray':['Never','Once a week','Every other day','Daily', 'More than once a day']},)
fig3.update_yaxes(title_text='Number of Those Surveyed')
fig3.update_xaxes(title_text='Eating Out Frequency')

fig4 = px.histogram(income, x="income", y=['diabetes','prediabetes','diabetesRisk'],
                    barmode='group',
                    histfunc='sum',)
fig4.update_layout(xaxis={'categoryorder':'array', 'categoryarray':['Unknown','less than 5,000','5,000 to 9,999','10,000 to 14,999', '15,000 to 19,999','Under 20,000','20,000 and Over','20,000 to 24,999',
                    '25,000 to 34,999','35,000 to 44,999','45,000 to 54,999','55,000 to 64,999','65,000 to 74,999','75,000 to 99,999','100,000 and Over']},
                    )
fig4.update_yaxes(title_text='Number of Those Surveyed')
fig4.update_xaxes(title_text='Income Bracket')

layout = html.Div(
    [
        dbc.Row(
            [
                dcc.Markdown('#### National Health and Nutrition Examination Survey (NHANES) Responders and Diabetes')
            ],
        ),
        dbc.Row(
            [
                dcc.Markdown('''
                    Here we looked at the Education Level, BMI groupings, The Frequency of Eating out, and Income Levels of NHANES respondents that have diabetes, are at risk for diabetes, and are described as pre-diabetic.
                ''')
            ],
        ),
        dbc.Row(
            [
            dbc.Col(
                dcc.Graph(
                    id='Education',
                    figure = fig1), width=6
                ),
            dbc.Col(
                dcc.Graph(
                    id='BMI',
                    figure = fig2
                ), width=6
                ),
            ],
        ),
        dbc.Row(
            [
            dbc.Col(
                dcc.Graph(
                    id='Food',
                    figure = fig3)
                ),
            dbc.Col(
                dcc.Graph(
                    id='Income',
                    figure = fig4
                ),
                ),
            ],
        ),
        
    ]
)