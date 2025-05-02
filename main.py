import pandas as pd
import json

def get_data(path):
    """
    :param path: Json file Path
    :return: Pandas DataFrames
    """
    with open(path,'r', encoding='utf-8') as file:
        json_data = json.load(file)
    return  pd.json_normalize(json_data)

path_locations = 'data/locations.json'
path_products = 'data/products.json'

#https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html
df_locations = get_data(path_locations)
df_products = get_data(path_products)

print(df_locations.head())
print(df_products.head())