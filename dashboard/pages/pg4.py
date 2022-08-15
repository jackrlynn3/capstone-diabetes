import dash
from dash import dcc, html

dash.register_page(__name__, name='Predicting Diabetes')

layout = html.Div(
    [
        dcc.Markdown('Can We Predict Diabetes?')
    ]
)