import pandas as pd
import json
import os

def get_data(path):
    """
    :param path: Json file Path
    :return: Pandas DataFrames
    """
    # Using os.path to Check if a File Exists https://blog.openreplay.com/python-check-if-file-exists/
    if not os.path.isfile(path):
        raise FileNotFoundError(f'{path} does not exist.')
    else:
        try:
            with open(path,'r', encoding='utf-8') as file:
                json_data = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f'JSON invalid on {path}')
        # https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html
    return  pd.json_normalize(json_data)

path_locations = 'data/locations.json'
path_products = 'data/products.json'

df_locations = get_data(path_locations)
df_products = get_data(path_products)
