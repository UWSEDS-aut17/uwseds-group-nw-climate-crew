
import os
import base64
import futurefish.futurefish as ff
import dash_core_components as dcc
import dash_html_components as html

APP_STYLE = {}
FULL_WIDTH = {'width': '100%'}
FULL_HEIGHT = {'height': '1000px'}
LEFT_JUSTIFY = {'width': '30%', 'float': 'left'}
RIGHT_JUSTIFY = {'width': '30%', 'float': 'right'}

INFORMATION = """
Climate change will have large effects on water resources all over
 the world. Our interactive FutureFish tool visualizes the predicted
 future viability of salmon species across the Pacific Northwest.
"""

OVERVIEW = """
In order to visualize the effect of climate change on salmon
 in the Pacific Northwest, we have estimated salmon viability
 as a function of future streamflow volume and temperature.
 Viability scores were separated into five categories, with
 green points representing locations with good fish viability,
 and red points representing locations with poor fish viability.
 The FutureFish map to the right displays the predicted fish
 viability score for four salmon species (select in dropdown menu)
 at each location in our dataset for two time periods in the
 next century (select with buttons below dropdown menu).
"""


def initialize_layout():
    logo_file = 'resources/images/logo_3.png'
    logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             logo_file)
    encoded_logo = base64.b64encode(open(logo_path, 'rb').read())
    header_cols = html.Div([
            html.Img(src='data:image/png;base64,{}'.format(
                encoded_logo.decode()), style={'height': '300px',
                                               'float': 'left',
                                               'padding': '5px 50px 5px'}),
            html.P(INFORMATION, style={'width': '400px', 'float': 'left',
                                       'padding': '100px 50px 100px 100px',
                                       'font-size': '1.2em',
                                       'margin': 'auto'}),
            html.Div([
                html.A('FutureFish source',
                       href='https://github.com/UWSEDS-aut17/uwseds-group'
                            '-nw-climate-crew',
                       style={'font-family': 'Montserrat',
                              'color': '#5792f2'}),
                html.P(),
                html.A('UWSEDS course page', href='http://uwseds.github.io/',
                       style={'font-family': 'Montserrat',
                              'color': '#5792f2'}),
                html.P(),
                html.A('NASA Climate Change information',
                       href='https://climate.nasa.gov/',
                       style={'font-family': 'Montserrat',
                              'color': '#5792f2'}),
                html.P()
                ], style={'float': 'right', 'padding': '100px 0px 30px 30px'})
            ])

    header_elements = [header_cols, html.Hr(style={'clear': 'both'})]
    header = html.Div(header_elements, className='header', style=FULL_WIDTH)

    info_elements = [
            html.H1(children='Overview'),
            html.Hr(),
            html.P(OVERVIEW)
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
                         style={'width': '25%'})

    map_elements = [
            html.H1(children='Salmon Viability in the Pacific NW'),
            html.Hr(),
            dcc.Graph(id='fish-map'),
            make_zoomlock_radio()
            ]
    mapper = html.Div(map_elements)
    right_pane = html.Div([mapper], className='column_right',
                          style={'width': '70%'})

    base_layout = html.Div([header, left_pane, right_pane],
                           className='futurefish')
    return base_layout


def make_species_dropdown():
    """Generates a dropdown bar to select fish species.
    @return dash.dcc Dropdown object
    """
    species = ff.DATA['Species'].unique()
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
    decades = ff.DATA['Decade'].unique()
    radio = dcc.RadioItems(
        id='decade',
        options=[{'label': i, 'value': i} for i in decades],
        value='2030-2059',
        labelStyle={'width': '40%', 'display': 'inline-block'},
        style={'padding-top': '10px', 'padding-bottom': '10px',
               'font-family': 'Montserrat'}
    )
    return radio


def make_zoomlock_radio():
    """Generates radio buttons for selecting whether or not
    to save map zoom/position settings between filtering steps.
    @return dash.dcc RadioItems object
    """
    radio = dcc.RadioItems(
        id='lock-zoom',
        options=[{'label': i, 'value': i}
                 for i in ['Lock View', 'Refresh View']],
        value='Lock View',
        style={'padding-top': '10px', 'padding-bottom': '10px',
               'font-family': 'Montserrat'}
    )
    return radio
