
import dash_core_components as dcc
import dash_html_components as html

APP_STYLE = {}
FULL_WIDTH = {'width': '100%'}
LEFT_JUSTIFY = {'width': '30%', 'float': 'left'}
RIGHT_JUSTIFY = {'width': '30%', 'float': 'right'}


def initialize_layout():
    header_elements = [
            html.Img(src='https://lh4.googleusercontent.com/7DX0EuNu06lSaE6Fx2Tx-O1QC0ZIWJKzKWgqH7zRbcs8thHKSZRoy6y5mte4lbV_Q9yAoAiDHiVypX037JKD=w1920-h1006',
                style={'display': 'block', 'margin': 'auto'}),
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
