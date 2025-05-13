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
def locations_map(df):
    return px.scatter_map(df,
                    lat='latitude',
                    lon='longitude',
                    hover_name='name',
                    hover_data='description',
                    custom_data='id',
                    center={"lat": 4.64, "lon": -74.3},
                    zoom=10,
                    size_max=40,
                    map_style='outdoors')
def histogram(df, x_column, title=None,x_label=None, y_label='Count'):
    """
    Generates a Plotly histogram for a given column in the DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data.
    - x_column (str): Name of the column to be used on the x-axis.
    - title (str, optional): Title of the histogram. Defaults to None.
    - x_label (str, optional): Label for the x-axis. Defaults to the column name.
    - y_label (str, optional): Label for the y-axis. Defaults to "Count".

    Returns:
    - fig (plotly.graph_objs._figure.Figure): A Plotly figure object representing the histogram.
    """
    #https://plotly.com/python/histograms/
    fig = px.histogram(
        df,
        x=x_column,
        title=title,
        labels={x_column: x_label or x_column}
    )

    fig.update_layout(
        xaxis_title=x_label or x_column,
        yaxis_title=y_label,
        bargap=0.2
    )

    return fig
def timeline(df, date_column, title=None, x_label='Date', y_label=''):
    """
    :param df: DataFrame containing the data
    :param date_column: Name of the datetime column
    :param title:  Chart title
    :param x_label: Label for the x-axis
    :param y_label: Label for the y-axis
    :return: A Plotly line chart
    """
    daily_counts = df[date_column].value_counts().sort_index()

    fig = px.line(
        x=daily_counts.index,
        y=daily_counts.values,
        title=title,
        labels={"x": x_label, "y": y_label}
    )

    fig.update_layout(xaxis_title=x_label, yaxis_title=y_label)
    return fig

app = Dash()

# Requires Dash 2.17.0 or later
app.layout = html.Div([
    html.Div([html.H1('LOCATIONS'),
              html.H3(f'The company has {locations.total()} stores.'),
              dcc.Graph(figure=locations_map(locations.df))
              ],
             id='id_locations',
             className= 'grid',
             style={'backgroundColor':'blue', 'width':'50%'}
             ),
    html.Div([html.H1('PRODUCTS'),
            html.P(f'The virtual store has {products.total()} products and {len(products.categories())} categories'),
            dcc.Graph(figure=histogram(
                products.df,
                'category.name',
                'Product per Category',
                'Category',
                'Number of Products'
            )
            ),
            html.H3(f'Most expensive product:'),
            html.P(f'Product: {products.costlier()[0]} cost: {products.costlier()[1]}'),
            html.H3(f'Cheaper product:'),
            html.P(f'Product: {products.cheaper()[0]} cost: {products.cheaper()[1]}'),
            dcc.Graph(figure=timeline(products.df,
                                      'creationAt',
                                      'Products Registration'))
              ],
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
