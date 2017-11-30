
import os
import base64
import dash_core_components as dcc
import dash_html_components as html

APP_STYLE = {}
FULL_WIDTH = {'width': '100%'}
LEFT_JUSTIFY = {'width': '30%', 'float': 'left'}
RIGHT_JUSTIFY = {'width': '30%', 'float': 'right'}


def initialize_layout():
    logo_file = 'resources/images/logo_3.png'
    logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), logo_file)
    encoded_logo = base64.b64encode(open(logo_path, 'rb').read())
    header_elements = [
            html.Img(src='data:image/png;base64,{}'.format(encoded_logo.decode()),
                     style={'height': '300px'}),
            html.Hr()
            ]
    header = html.Div(header_elements, className='header', style=FULL_WIDTH)

    info_elements = [
            html.H1(children='Information'),
            html.Hr()
            ]
    information = html.Div(info_elements, className='information_panel')
    selector_elements = [
            html.H1(children='Selector stuff'),
            html.Hr()
            ]
    selector = html.Div(selector_elements, className='selector')
    left_pane = html.Div([information, selector],
                         className='column_left')

    map_elements = [
            html.H1(children='Map element'),
            html.Hr()
            ]
    mapper = html.Div(map_elements)
    right_pane = html.Div([mapper], className='column_right')

    base_layout = html.Div([header, left_pane, right_pane], className='futurefish')
    return base_layout
