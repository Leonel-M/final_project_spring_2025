"""
A Minimal Dash App from https://dash.plotly.com/minimal-app
"""

from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from data import df_locations, df_products

"""
scatter_map configuration https://docs.sisense.com/main/SisenseLinux/scatter-map.htm
"""
locations_map = px.scatter_map(df_locations,
                    lat='latitude',
                    lon='longitude',
                    hover_name='name',
                    hover_data='description',
                    custom_data='id',
                    center={"lat": 4.64, "lon": -74.3},
                    zoom=10,
                    size_max=40,
                    map_style='outdoors')

app = Dash()

# Requires Dash 2.17.0 or later
app.layout = html.Div([
    dcc.Graph(figure=locations_map)
])


if __name__ == '__main__':
    app.run(debug=True)
