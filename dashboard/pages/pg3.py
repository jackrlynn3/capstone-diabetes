import dash
from dash import dcc, html

dash.register_page(__name__, name='NHANES findings')

layout = html.Div(
    [
        dcc.Markdown('# Under Concstruction')
    ]
)