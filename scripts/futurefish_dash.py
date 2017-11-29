import dash
import futurefish

if __name__ == '__main__':
    app = dash.Dash('Future Fish')
    app.layout = futurefish.dashboard.initialize_layout()
    app.run_server()
