"""
A Minimal Dash App from https://dash.plotly.com/minimal-app
"""

from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from data import locations, products, users

"""
scatter_map configuration https://docs.sisense.com/main/SisenseLinux/scatter-map.htm
"""
locations_map = px.scatter_map(locations.df,
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
    html.Div([html.H1('LOCATIONS'),dcc.Graph(figure=locations_map)],
             id='id_locations',
             className= 'grid',
             style={'backgroundColor':'blue', 'width':'50%'}
             ),
    html.Div([html.H1('PRODUCTS')],
             id='id_products',
             className='grid',
             style={'backgroundColor': 'red', 'width': '50%'}
             ),
    html.Div([html.H1('USERS')],
             id='id_users',
             className='grid',
             style={'backgroundColor': 'yellow', 'width': '100%'}
             ),

])


if __name__ == '__main__':
    app.run(debug=True)
