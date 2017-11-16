import dash
import futurefish as ff


if __name__ == '__main__':
    app = dash.Dash('Future Fish')
    app.layout = ff.dashboard.initialize_layout()
    app.run_server()
