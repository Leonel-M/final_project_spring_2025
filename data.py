import pandas as pd
import json
import os

class DataFrame:
    def __init__(self, in_path):
        self.path = in_path
        self.df = self.get_data()

    def total(self):
        """
        :return:  Total amount of data per column 'id'
        """
        return len(self.df['id'].count())

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

    def get_info(self):
        """
        :return: DataFrame information
        """
        print(f'{self.df.info()}')
        return

class Product(DataFrame):
    def __init__(self,in_path):
        super().__init__(in_path)

    def average(self):
        """
        :return: Average price of products.
        """
        return self.df['price'].mean()

    def costlier(self):
        """
        :return:  the most expensive product (title and price)
        """
        # https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmax.html

        id_max = self.df['price'].idxmax()
        product = self.df.loc[id_max,'title']
        price = self.df.loc[id_max,'price']
        print(f'{product} is the most expensive product, cost: {price}')
        return product, price

    def cheaper(self):
        """
        :return: the most cheap product (title and price)
        """
        id_min = self.df['price'].idxmin()
        product = self.df.loc[id_min, 'title']
        price = self.df.loc[id_min, 'price']
        print(f'{product} is the most cheaper product, cost: {price}')
        return product, price

path_locations = 'data/locations.json'
path_products = 'data/products.json'
path_users = 'data/users.json'

locations = DataFrame(path_locations)
products = Product(path_products)
users = DataFrame(path_users)


