import dash
import futurefish

css_files = [
        'https://cdn.rawgit.com/UWSEDS-aut17/uwseds-group-nw-climate-crew/master/futurefish/resources/futurefish.css',
        'https://livvkit.github.io/LIVVkit/css/livv.css'
        ]

if __name__ == '__main__':
    app = dash.Dash('Future Fish')
    app.layout = futurefish.dashboard.initialize_layout()
    for css in css_files:
        app.css.append_css({"external_url": css})
    app.server.run(threaded=True)
