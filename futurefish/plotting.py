import plotly.graph_objs as go
import futurefish.futurefish as ff


def make_colorscale(scl0='rgb(255, 6, 6)', scl20='rgb(255, 153, 51)',
                    scl40='rgb(255, 255, 51)', scl60='rgb(128, 255, 0)',
                    scl80='rgb(0, 102, 0)'):
    """Generates a discrete color scale for the map graphic.
    @param scl0 - color string for the minimum value
    @param scl20 - color string for the 20% value
    @param scl40 - color string for the 40% value
    @param scl60 - color string for the 60% value
    @param scl80 - color string for the 80% value
    @return 2D array containing scale-color pairings
    """
    return [[0, scl0], [0.2, scl0], [0.2, scl20],
            [0.4, scl20], [0.4, scl40], [0.6, scl40],
            [0.6, scl60], [0.8, scl60], [0.8, scl80], [1.0, scl80]]


def generate_map(species, decade):
    """Generates an interactive plot using mapbox with salmon
       viability displayed as colored points on the map.
    """
    data_subset = ff.DATA[(ff.DATA['Species'] == species)
                          & (ff.DATA['Decade'] == decade)]
    scale = make_colorscale()
    marker_dict = {
        'size': 10,
        'symbol': 'circle',
        'colorscale': scale,
        'cmin': 1,
        'color': data_subset['Viability'],
        'cmax': data_subset['Viability'].max(),
        'colorbar': dict(title="Salmon Viability",
                         tickmode='array',
                         tickvals=[1.4, 2.2, 3.0, 3.8, 4.6],
                         ticktext=['Yikes!', 'Nope', 'Hmm?',
                                   'Good', 'Great'],
                         ticks='outside',
                         titlefont={'family': 'Montserrat', 'size': 14},
                         tickfont={'family': 'Montserrat', 'size': 12})
        }
    return [go.Scattermapbox(
            lon=data_subset['Longitude'], lat=data_subset['Latitude'],
            mode='markers', marker=marker_dict, text=data_subset['Basin'])]
