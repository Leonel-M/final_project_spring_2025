import plotly.express as px
from dash import Dash, html,dcc

from data import locations, products, users

def locations_map(df):
    """
    :param df: DataFrame containing the data
    :return: Map with points according to longitude and latitude
    """
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

def header():
    """
    :return:  Dash html.Header component containing the HEADER layout
    """
    return html.Header([ html.Img(src='https://fakeapi.platzi.com/_astro/icon.BNMhJCSt.png', alt='platzi_icon', id='icon'),
                  html.H1('Platzi Fake Store App Dashboard'),
    ], id='id_header')

def locations_layout():
    """
    :return: Dash html.Div component containing the locations layout
    """
    return    html.Div([html.H2('LOCATIONS'),
              html.P(f'The company has {locations.total()} stores.'),
              dcc.Graph(figure=locations_map(locations.df))
              ],
             id='id_locations',
             className= 'grid',
             )

def users_layout():
    """
    :return: Dash html.Div component containing the users layout
    """
    return html.Div([html.H2('USERS'),

              html.P(f'the online store has {users.total()} registered users. {users.admins} administrators and {users.customers} customers.'),
              dcc.Graph(figure=timeline(users.df[users.df['role'] == 'customer'],
                                        # Only show users with customer role inside df
                                        'creationAt',
                                        'Registration of customers in the store'))
              ],
             id='id_users',
             className='grid'
             )

def products_layout():
    """
    :return: Dash html.Div component containing the products layout
    """
    return html.Div([
        html.Div([html.H2('PRODUCTS'),
            html.P(f'The virtual store has {products.total()} products and {len(products.categories())} categories'),
            dcc.Graph(figure=histogram(
                products.df,
                'category.name',
                'Product per Category',
                'Category',
                'Number of Products'
            )
            ),], id='category'),
        html.Div([
            html.Div([
                html.H3(f'Most expensive product:'),
                html.P(f'Product: {products.expensive_product[0]} cost: {products.expensive_product[1]}'),],style={'width': '49%', 'display': 'inline-block', 'verticalAlign': 'top'}),
            html.Div([
                html.H3(f'Cheaper product:'),
                html.P(f'Product: {products.cheap_product[0]} cost: {products.cheap_product[1]}'),],style={'width': '49%', 'display': 'inline-block', 'verticalAlign': 'top'}),

            dcc.Graph(figure=timeline(products.df,
                                      'creationAt',
                                      'Products Registration'))], id='product'),
              ],
             id='id_products',
             className='grid'
             )