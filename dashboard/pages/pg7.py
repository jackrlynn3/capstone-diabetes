import dash
from dash import Dash, dcc, html, Input, Output
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
from dash import html, dcc
import pymssql

dash.register_page(__name__, name='DL Prediction')

# Create training_card
def createTrainingCard(header_md, card_images_links, card_image_titles, card_image_parts, analysis_md):
    training_card = []

    # Fill in header
    header = dbc.Row([dcc.Markdown(header_md)])
    training_card.append(header)

    # Create cards
    cards_contents = []
    for i in range(len(card_images_links)):

        # Get components
        image = card_images_links[i]
        title = card_image_titles[i]
        parts = card_image_parts[i]

        # For the card
        this_card = dbc.Col([dbc.Card([dbc.CardImg(src=image, top=True),
            dbc.CardBody([dcc.Markdown(title)])], style={"width": "100%"})],
            style={"flex-grow": str(parts)}
        ) 

        # Add card
        cards_contents.append(this_card)
    
    # Create row for contents
    training_card.append(dbc.Row(cards_contents))

    # Add description
    description = dbc.Row([dcc.Markdown(analysis_md)])
    training_card.append(description)

    # Return card
    return training_card

# Cards contents

# Delay test
header_delay = '''
    ## Time Delay 
    Time delays are varied by 5 minute intervals from 5 to 120 mins; this will determine how long in the future the model can successfully predict.
'''
images_delay = ["https://github.com/jackrlynn3/capstone-diabetes/blob/main/visualizations/deep-learning/time-delay-2.png?raw=true",
    "https://raw.githubusercontent.com/jackrlynn3/capstone-diabetes/main/visualizations/deep-learning/time-delay-1.png?raw=true"]
titles_delay = ["### Evaluation of Time Delay Models", "### Comparison of Time Delay Models to Truth"]
parts_delay = ['1', '2']
analysis_delay = '''
    Loss linearly increases as the distance between prediction value and input values increases;
    the best balance between loss and substantial blood forecasting is 30 min. Time delays do not
    have any non-neglible effects on training time. All models perform best during times of change
    and worst at predicting the specific peaks and valleys of the traces, typically
    underpredicting them. Overall, the 30 min delay model has the best fidelty to truth traces.
'''
delay_card = createTrainingCard(header_delay, images_delay, titles_delay, parts_delay, analysis_delay)
print(delay_card)

layout = html.Div(
    [
        dbc.Row(
            [
                # Intro section
                dbc.Col(
                    [
                        dcc.Markdown('''
                            # Blood Glucose Levels Prediction using Deep Learning
                            Tracking blood glucose levels is essential to modern diabetes care. Deep learning time series models are used to predict blood glucose levels of Type-1 diabetes patients 30 minutes ahead. Additionally, patients are notified when their blood glucose levels exceed 300 mmol/L, which is considered dangerously high.
                        ''')
                    ],
                ),
                
                # Model introduction
                dbc.Col(
                    [
                        dcc.Markdown('''
                            ## Optimized Model
                            <Include description of model>
                        ''')
                    ],
                )
            ]
        ),

        # MODEL OPTIMIZATION
        dbc.Row(delay_card)
    ]
)