import dash
import futurefish
import futurefish.dashboard as db
import plotly.graph_objs as go

css_files = [
        'https://cdn.rawgit.com/UWSEDS-aut17/uwseds-group-nw-climate-crew/master/futurefish/resources/futurefish.css',
        'https://fonts.googleapis.com/css?family=Domine|Montserrat'
        ]
app = dash.Dash('Future Fish')
app.layout = futurefish.dashboard.initialize_layout()
for css in css_files:
    app.css.append_css({"external_url": css})


@app.callback(
    dash.dependencies.Output('fish-map', 'figure'),
    [dash.dependencies.Input('species', 'value'),
     dash.dependencies.Input('decade', 'value')]
)
def update_map(species, decade):
    data_subset = db.DATA[(db.DATA['Species'] == species) & (db.DATA['Decade'] == decade)]
    scale = db.make_colorscale()
    marker_dict = {
        'size': 8,
        'symbol': 'circle',
        'colorscale': scale,
        'cmin': 1,
        'color': data_subset['Viability'],
        'cmax': data_subset['Viability'].max(),
        'colorbar': dict(title="Viability of Salmon Life",
                         tickmode = 'array',
                         tickvals = [1.4,2.2,3.0,3.8,4.6],
                         ticktext = ['Great','Good','Mmm?','Nope','Yikes!'],
                         ticks = 'outside')
    }
    return {
        'data': [go.Scattermapbox(
            lon=data_subset['Longitude'],
            lat=data_subset['Latitude'],
            mode='markers',
            marker=marker_dict,
            text=data_subset['Basin']
        )],
        'layout': go.Layout(
            height=db.MAP_HEIGHT,
            width=db.MAP_WIDTH,
            margin=db.MAP_MARGIN,
            font=db.MAP_FONT,
            paper_bgcolor=db.MAP_BG_COLOR,
            mapbox=dict(accesstoken=db.TOKEN,
                        bearing=db.MAP_BEARING,
                        center=db.MAP_CENTER,
                        pitch=db.MAP_PITCH,
                        zoom=db.MAP_ZOOM,
                        style='light')
        )
    }


if __name__ == '__main__':
    app.server.run(threaded=True)
