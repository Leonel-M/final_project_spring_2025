"""
A Minimal Dash App from https://dash.plotly.com/minimal-app
"""

from dash import Dash, html, dcc, callback, Output, Input
from components import locations_map, histogram, timeline, locations_layout, users_layout, products_layout, header
from data import locations, products, users

"""
scatter_map configuration https://docs.sisense.com/main/SisenseLinux/scatter-map.htm
"""

app = Dash()

# Requires Dash 2.17.0 or later
app.layout = html.Div([
    header(),
    locations_layout(),   # --- Div LOCATIONS
    users_layout(),  # --- Div USERS
    products_layout(),  # --- Div PRODUCTS
])


if __name__ == '__main__':
    app.run(debug=True)
