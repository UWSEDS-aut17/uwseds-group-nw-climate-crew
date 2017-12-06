
import os
import base64
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


APP_STYLE = {}
FULL_WIDTH = {'width': '100%'}
LEFT_JUSTIFY = {'width': '30%', 'float': 'left'}
RIGHT_JUSTIFY = {'width': '30%', 'float': 'right'}

DATA_FILE = 'model/fish_vulnerability.csv'
CWD = os.path.dirname(os.path.abspath(__file__))
DATA_STR = os.path.join(CWD, DATA_FILE)
DATA = pd.read_csv(DATA_STR)
TOKEN = 'pk.eyJ1IjoibWticmVubmFuIiwiYSI6ImNqYW12OGxjYjM1MXUzM28yMXhpdWE3NW0' \
        'ifQ.EljNVtky3qEFfvJL80RgMQ'

MAP_HEIGHT = 500
MAP_WIDTH = 700
MAP_MARGIN = dict(t=0, b=0, l=0, r=0)
MAP_FONT = dict(color='#FFFFFF', size=11)
MAP_BG_COLOR = '#50667f'
MAP_BEARING = 0
MAP_CENTER = dict(lat=46, lon=-119)
MAP_PITCH = 0
MAP_ZOOM = 4.5

def initialize_layout():
    logo_file = 'resources/images/logo_3.png'
    logo_path = os.path.join(CWD, logo_file)
    encoded_logo = base64.b64encode(open(logo_path, 'rb').read())
    header_elements = [
            html.Img(src='data:image/png;base64,{}'.format(
                encoded_logo.decode()), style={'height': '300px'}),
            html.Hr()
            ]
    header = html.Div(header_elements, className='header', style=FULL_WIDTH)

    info_elements = [
            html.H1(children='Overview'),
            html.Hr(),
            html.P("Climate change will have large effects on water resources"
                   " all over the world. Our interactive FutureFish tool "
                   "visualizes the predicted future viability of salmon "
                   "species across the Pacific Northwest.")
            ]
    information = html.Div(info_elements, className='information_panel')
    selector_elements = [
            html.Hr(),
            html.Div(make_species_dropdown(),
                     style={'padding-top': '10px', 'padding-bottom': '10px',
                            'font-family': 'Montserrat'}),
            make_decade_radio()
            ]
    selector = html.Div(selector_elements, className='selector')
    left_pane = html.Div([information, selector],
                         className='column_left',
                         style={'width': '42%'})

    map_elements = [
            html.H1(children='Salmon Viability in the Pacific NW'),
            html.Hr(),
            dcc.Graph(id='fish-map')
            ]
    mapper = html.Div(map_elements)
    right_pane = html.Div([mapper], className='column_right',
                          style={'width': '53%'})

    base_layout = html.Div([header, left_pane, right_pane],
                           className='futurefish')
    return base_layout


def make_colorscale(scl0='rgb(0, 102, 0)', scl20='rgb(128, 255, 0)',
                    scl40='rgb(255, 255, 51)', scl60='rgb(255, 153, 51)',
                    scl80='rgb(255, 6, 6)'):
    """Generates a discrete color scale for the map graphic.
    @param scl0 - color string for the minimum value
    @param scl20 - color string for the 20% value
    @param scl40 - color string for the 40% value
    @param scl60 - color string for the 60% value
    @param scl80 - color string for the 80% value
    @return 2D array containing scale-color pairings
    """
    return [[0, scl0], [0.2, scl0], [0.2, scl20], [0.4, scl20], [0.4, scl40],
            [0.6, scl40], [0.6, scl60], [0.8, scl60], [0.8, scl80],
            [1.0, scl80]]


def make_species_dropdown():
    """Generates a dropdown bar to select fish species.
    @return dash.dcc Dropdown object
    """
    species = DATA['Species'].unique()
    dd = dcc.Dropdown(
        id='species',
        options=[{'label': i, 'value': i} for i in species],
        value='Chinook'
    )
    return dd


def make_decade_radio():
    """Generates radio buttions for selecting the decade for
    which to display data.
    @return dash.dcc RadioItems object
    """
    decades = DATA['Decade'].unique()
    radio = dcc.RadioItems(
        id='decade',
        options=[{'label': i, 'value': i} for i in decades],
        value='2030-2059',
        labelStyle={'width': '30%','display': 'inline-block'},
        style={'padding-top': '10px', 'padding-bottom': '10px',
               'font-family': 'Montserrat'}
    )
    return radio
