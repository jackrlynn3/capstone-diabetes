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
def createTrainingCard(header_md, card_images_links, card_image_titles, card_image_parts, analysis_md, overwrite=False):
    training_card = []

    # Fill in header
    header = dbc.Row([dcc.Markdown(header_md)])
    training_card.append(header)

    # Create cards
    cards_contents = []
    num_cards = len(card_images_links)
    for i in range(num_cards):

        # Get components
        image = card_images_links[i]
        title = card_image_titles[i]
        parts = card_image_parts[i]

        # For the card
        width = "100%"
        if (overwrite):
            width = "40%"
        this_card = dbc.Col([dbc.Card([dbc.CardImg(src=image, top=True),
            dbc.CardBody([dcc.Markdown(title)])], style={"width": width})],
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

# GRAPHIC CARDS

# Delay test
header_delay = '''
    Time delay describes the gap between when sample blood glucose levels are taken and when the prediction
    being made (e.g., predicting 30 minutes into the future). Time delays are varied by 5 min intervals, ranging
    from 5 to 120 min.
'''
images_delay = ["https://github.com/jackrlynn3/capstone-diabetes/blob/main/visualizations/deep-learning/time-delay-2.png?raw=true",
    "https://raw.githubusercontent.com/jackrlynn3/capstone-diabetes/main/visualizations/deep-learning/time-delay-1.png?raw=true"]
titles_delay = ["#### **Evaluation of Time Delay Models**", "#### **Comparison of Time Delay Models to Truth**"]
parts_delay = ['1', '2']
analysis_delay = '''
    #### **Evaluation**
    Loss linearly increases as the distance between prediction value and input values increases;
    the best balance between loss and substantial blood forecasting is 30 min. Time delays do not
    have any non-neglible effects on training time. All models perform best during times of change
    and worst at predicting the specific peaks and valleys of the traces, typically
    underpredicting them. Overall, the 30 min delay model has the best fidelty to truth traces.
'''
delay_card = createTrainingCard(header_delay, images_delay, titles_delay, parts_delay, analysis_delay)

# Width test
header_window = '''
    Window sizes describes how many previous inputs are considered for the current estimation (e.g., using
    the 10 previous inputs for the current estimation). Window sizes are varied by 5 previous points, ranging
    from 5 to 50 previous timepoints.
'''
images_window = ["https://github.com/jackrlynn3/capstone-diabetes/blob/main/visualizations/deep-learning/width-1.png?raw=true",
    "https://github.com/jackrlynn3/capstone-diabetes/blob/main/visualizations/deep-learning/width-2.png?raw=true"]
titles_window = ["#### **Evaluation of Window Size Models**", "#### **Comparison of Window Size Models to Truth**"]
parts_window = ['1', '2']
analysis_window = '''
    #### **Evaluation**
    Model accuracy remains consistently high for all window sizes above 10, with minor training time costs for
    increasing window size. A window size of 20 previous points is used to maximize accuracy without too much
    computational cost.
'''
window_card = createTrainingCard(header_window, images_window, titles_window, parts_window, analysis_window)

# Training test
header_train = '''
    Training time describes how many training epochs are required for the model to be sufficiently trained.
    Training times are varied between 1 and 50 to determine how much training is required to minimize loss.
'''
images_train = ["https://github.com/jackrlynn3/capstone-diabetes/blob/main/visualizations/deep-learning/training-time-1.png?raw=true"]
titles_train = ["#### **Evaluation of Training Time Models**"]
parts_train = ['1']
analysis_train = '''
    #### **Evaluation**
    Loss rounds off at around 6 epochs, though some improvements occur up until 30. Training time linearly increases
    with the number of epochs. The ideal number of training epochs chosen is 30 to balance both training time and
    loss reduction.
'''
train_card = createTrainingCard(header_train, images_train, titles_train, parts_train, analysis_train, overwrite=True)

# Layer composition test
header_layers = '''
    Layer composition describes the number and types of neural network layers used in the DL model. Two layer
    types are evaluated here--long short-term memory (LSTM) and gated recurrent unit (GRU)--for their strength
    with time-series data. The number of neural network layers is also evaluated; the following models are tested:
    1. 1 to 4 GRU layers
    2. 1 to 4 LSTM layers
    3. 2 to 4 GRU/LSTM mixed layers
'''
images_layers = ["https://github.com/jackrlynn3/capstone-diabetes/blob/main/visualizations/deep-learning/layer-1.png?raw=true"]
titles_layers = ["#### **Evaluation of Layer Composition Models**", "#### **Comparison of Layer Composition Models to Truth**"]
parts_layers = ['1']
analysis_layers = '''
    #### **Evaluation**
    In all cases, 1 to 2 layers produced the most optimal layer formation, though any more dramatically increased loss.
    There is a neglible difference between LSTM and GRU models, so the 2-layer mixed GRU/LSTM is chosen. Training time 
    does increase with the number of layers, but there is not a large difference between 1 and 2 layers.
'''
layers_card = createTrainingCard(header_layers, images_layers, titles_layers, parts_layers, analysis_layers)

# Optimal model
header_optimal = '''
    The optimal model is trained to have the following parameters:
    1. Prediction 30 min into future
    2. Window size of 20
    3. 30 training epochs
    4. 1 LSTM layer; 1 GRU layer
'''
images_optimal = ["https://github.com/jackrlynn3/capstone-diabetes/blob/main/visualizations/deep-learning/optimum-model-1.png?raw=true",
    "https://github.com/jackrlynn3/capstone-diabetes/blob/main/visualizations/deep-learning/optimum-model-2.png?raw=true"]
titles_optimal = ["#### **Evaluation of Optimal Model over 30 Training Epochs**",
    "#### **Comparison of Optimal Model to Truth**"]
parts_optimal = ['1', '2']
analysis_optimal = '''
    #### **Evaluation**
    This model took 299 sec to train and has a result mean squared error loss of 1337. Note that this model is not
    an absolute minimization of loss but rather a balance of training time, loss, and predictive power into the future.
'''
optimal_card = createTrainingCard(header_optimal, images_optimal, titles_optimal, parts_optimal, analysis_optimal)

########################################################################################

# PAGE LAYOUT

layout = html.Div(
    [
        dbc.Row(
            [
                # Intro section
                dbc.Col(
                    [
                        dcc.Markdown('''
                            # **Blood Glucose Levels Prediction using Deep Learning**
                            Tracking blood glucose levels is essential to modern diabetes care. Deep learning time series models are used to predict blood glucose levels of Type-1 diabetes patients 30 minutes ahead. Additionally, patients are notified when their blood glucose levels exceed 300 mmol/L, which is considered dangerously high.
                        ''')
                    ],
                ),
                
                # Model introduction
                dbc.Col(
                    [
                        dcc.Markdown('''
                            ## **Optimized Model**
                            <Include description of model>
                        ''')
                    ],
                )
            ]
        ),

        dbc.Row(
            [
                dcc.Markdown('''
                    ## **Model Optimization**
                    The deep learning model is optimized for four terms: (1) **Window Size:** number of previously
                    used datapoints; (2) **Time Delay:** how far ahead the model predicts in the future; (3)
                    **Training Time:** number of training epochs needed to fully train model; and (4) **Layer Composition:**
                    number and type of layers used in the model. Additionally, the most **Optimal Model** is evaluated for loss,
                    training time, and faithfulness to truth.
                '''),

            ]
        ),

        dbc.Row(
            [
                dcc.Dropdown(['Optimal Model', 'Window Size', 'Time Delay', 'Training Time', 'Layer Composition'],
                'Optimal Model', id="select-opt")
            ],
            style={'fontSize':28, 'textAlign':'left', 'font-weight':'bold'}
        ),

        # MODEL OPTIMIZATION
        dbc.Row(id='model-opt')
    ]
)

@callback(
     Output('model-opt', 'children'),
    [Input(component_id='select-opt', component_property='value')]
)
def show_graph(opt_select):
    if (opt_select == 'Window Size'):
        return window_card
    elif (opt_select == 'Time Delay'):
        return delay_card
    elif (opt_select == 'Training Time'):
        return train_card
    elif (opt_select == 'Optimal Model'):
        return optimal_card
    elif (opt_select == 'Layer Composition'):
        return layers_card