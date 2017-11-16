
import dash_core_components as dcc
import dash_html_components as html

FULL_WIDTH = {'width': '100%'}
LEFT_JUSTIFY = {'float': 'left'}
RIGHT_JUSTIFY = {'float': 'right'}


def initialize_layout():
    header_elements = [
            html.H1(children='Fish Finder'),
            html.Hr()
            ]
    header = html.Div(header_elements, style=FULL_WIDTH)

    info_elements = [
            html.H1(children='Information'),
            html.Hr()
            ]
    information = html.Div(info_elements)
    selector_elements = [
            html.H1(children='Selector stuff'),
            html.Hr()
            ]
    selector = html.Div(selector_elements)
    left_pane = html.Div([information, selector],
                         style=LEFT_JUSTIFY)

    map_elements = [
            html.H1(children='Map element'),
            html.Hr()
            ]
    mapper = html.Div(map_elements)
    right_pane = html.Div([mapper], style=RIGHT_JUSTIFY)

    base_layout = html.Div([header, left_pane, right_pane])
    return base_layout
