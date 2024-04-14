from dash import Dash, html
from flask import Flask

# Exposing the Flask Server to enable configuring it for logging in
server = Flask(__name__)
app = Dash(__name__)

app.layout = html.Div([html.Div(children="Hello Data")])

if __name__ == "__main__":
    app.run_server(debug=True)
