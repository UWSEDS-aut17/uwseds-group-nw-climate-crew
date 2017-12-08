
import plotly.graph_objs as go
import futurefish.plotting as fishplt
from dash.dependencies import Input, Output, State

TOKEN = ('pk.eyJ1IjoibWticmVubmFuIiwiYSI6'
         'ImNqYW12OGxjYjM1MXUzM28yMXhpdWE'
         '3NW0ifQ.EljNVtky3qEFfvJL80RgMQ')

MAP_HEIGHT = 500
MAP_WIDTH = 700
MAP_MARGIN = dict(t=0, b=0, l=0, r=0)
MAP_FONT = dict(color='#000000', size=11)
MAP_BG_COLOR = '#FFFFFF'
MAP_BEARING = 0
MAP_CENTER = dict(lat=46, lon=-119)
MAP_PITCH = 0
MAP_ZOOM = 4.5
MAPBOX_DICT = dict(accesstoken=TOKEN,
                   bearing=MAP_BEARING,
                   center=MAP_CENTER,
                   pitch=MAP_PITCH,
                   zoom=MAP_ZOOM,
                   style='light')


def initialize_callbacks(app):
    @app.callback(
        Output('fish-map', 'figure'),
        [Input('species', 'value'),
         Input('decade', 'value'),
         Input('lock-zoom', 'value')],
        [State('fish-map', 'relayoutData')])
    def update_map(species, decade, zoomlock, relayout):
        if relayout and ('mapbox' in relayout.keys()) \
                and zoomlock == 'Lock View':
            mapbox_dict = update_mapbox_dict(relayout)
        else:
            mapbox_dict = MAPBOX_DICT
        layout = go.Layout(margin=MAP_MARGIN, font=MAP_FONT,
                           paper_bgcolor=MAP_BG_COLOR,
                           mapbox=mapbox_dict)
        return {'data': fishplt.generate_map(species, decade),
                'layout': layout}


def update_mapbox_dict(relayout):
    """Generates a new dictionary of mapbox settings from the
    relayout data returned between interactive calls.
    @return dictionary of mapbox settings
    """
    mb = relayout['mapbox']
    return dict(accesstoken=TOKEN, bearing=mb['bearing'], center=mb['center'],
                pitch=mb['pitch'], zoom=mb['zoom'], style='light')