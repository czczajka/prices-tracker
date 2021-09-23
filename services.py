import os
from schemas import product
import pandas as pd


def find_product_names():
    product_names = []
    files = os.listdir('static/graphs')
    for file in files:
        product_names.append(file.replace('.html', ''))
    return product_names


def set_data(product_name: str):
    product_data = product
    product_data.name = product_name

    df = pd.read_csv('csv-db/' + product_data.name + '.csv')

    product_data.max = df['price'].max()
    product_data.min = df['price'].min()
    product_data.end = df['date'].max()
    product_data.start = df['date'].min()

    oldest = df[df['date'] == product_data.start]
    newest = df[df['date'] == product_data.end]
    product_data.change = round(get_change(oldest.iloc[0]['price'], newest.iloc[0]['price']), 2)

    return product_data


def find_product_by_name(name: str):
    products = find_product_names()
    for element in products:
        if element == name:
            return name
    return None


def get_change(oldest, newest):
    if oldest == newest:
        return 100.0
    try:
        return ((newest - oldest) / oldest) * 100.0
    except ZeroDivisionError:
        return 0.0
