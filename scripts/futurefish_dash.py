import dash
import futurefish
import futurefish.dashboard as db
import futurefish.interactions as fi

css_files = [
        'https://cdn.rawgit.com/UWSEDS-aut17/uwseds-group-nw-climate-crew/master/futurefish/resources/futurefish.css',
        'https://fonts.googleapis.com/css?family=Domine|Montserrat'
        ]

if __name__ == '__main__':
    app = dash.Dash('Future Fish')
    for css in css_files:
        app.css.append_css({"external_url": css})
    app.layout = db.initialize_layout()
    fi.initialize_callbacks(app)
    app.server.run(threaded=True)
