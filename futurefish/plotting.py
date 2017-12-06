
import plotly.graph_objs as go
import futurefish.futurefish as ff


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
    return [[0, scl0], [0.2, scl0], [0.2, scl20],
            [0.4, scl20], [0.4, scl40], [0.6, scl40],
            [0.6, scl60], [0.8, scl60], [0.8, scl80], [1.0, scl80]]


def generate_map(species, decade):
        data_subset = ff.DATA[(ff.DATA['Species'] == species)
                              & (ff.DATA['Decade'] == decade)]
        scale = make_colorscale()
        marker_dict = {
            'size': 8,
            'symbol': 'circle',
            'colorscale': scale,
            'cmin': 1,
            'color': data_subset['Viability'],
            'cmax': data_subset['Viability'].max(),
            'colorbar': dict(title="Viability of Salmon Life", tick0=0, dtick=1)
        }
        return [go.Scattermapbox(
            lon=data_subset['Longitude'], lat=data_subset['Latitude'],
            mode='markers', marker=marker_dict, text=data_subset['Basin'])]
