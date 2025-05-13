import pandas as pd
import json
import os

class DataFrame:
    def __init__(self, in_path):
        self.path = in_path
        self.df = self.get_data()

    def get_data(self):
        """
        :return: Pandas DataFrames
        """
        # Using os.path to Check if a File Exists https://blog.openreplay.com/python-check-if-file-exists/
        if not os.path.isfile(self.path):
            raise FileNotFoundError(f'{self.path} does not exist.')
        else:
            try:
                with open(self.path,'r', encoding='utf-8') as file:
                    json_data = json.load(file)
            except json.JSONDecodeError as e:
                raise ValueError(f'JSON invalid on {self.path}')
            # https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html
        return  pd.json_normalize(json_data)

    def info(self):
        print(f'')
path_locations = 'data/locations.json'
path_products = 'data/products.json'
path_users = 'data/users.json'

locations = DataFrame(path_locations)
products = DataFrame(path_products)
users = DataFrame(path_users)


