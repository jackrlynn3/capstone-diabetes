import dash
from dash import dcc, html

dash.register_page(__name__, name='Daibetes in the U.S.')

layout = html.Div(
    [
        dcc.Markdown('# Under Concstruction')
    ]
)