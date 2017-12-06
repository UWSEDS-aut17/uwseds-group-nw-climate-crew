
import os
import base64
import futurefish.futurefish as ff
import dash_core_components as dcc
import dash_html_components as html


APP_STYLE = {}
FULL_WIDTH = {'width': '100%'}
LEFT_JUSTIFY = {'width': '30%', 'float': 'left'}
RIGHT_JUSTIFY = {'width': '30%', 'float': 'right'}

INFORMATION = """
"""


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
            html.Hr(),
            make_species_dropdown(),
            make_decade_radio()
            ]
    selector = html.Div(selector_elements, className='selector')
    left_pane = html.Div([information, selector],
                         className='column_left',
                         style={'width': '42%'})

    map_elements = [
            html.H1(children='Map element'),
            html.Hr(),
            dcc.Graph(id='fish-map')
            ]
    mapper = html.Div(map_elements)
    right_pane = html.Div([mapper], className='column_right',
                          style={'width': '53%'})

    base_layout = html.Div([header, left_pane, right_pane], className='futurefish')
    return base_layout


def make_species_dropdown():
    """Generates a dropdown bar to select fish species.
    @return dash.dcc Dropdown object
    """
    species = ff.DATA['Species'].unique()
    dd = dcc.Dropdown(
        id='species', value='A',
        options=[{'label': i, 'value': i} for i in species],
    )
    return dd


def make_decade_radio():
    """Generates radio buttions for selecting the decade for which to display data.
    @return dash.dcc RadioItems object
    """
    decades = ff.DATA['Decade'].unique()
    radio = dcc.RadioItems(
        id='decade', value='2030-2059',
        options=[{'label': i, 'value': i} for i in decades],
        labelStyle={'width': '30%', 'display': 'inline-block'}
    )
    return radio
