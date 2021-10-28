import os
from schemas import product
import pandas as pd


def find_items_names():
    names = []
    files = os.listdir('data/')
    for file in files:
        names.append(file.replace('.csv', ''))
    names = sorted(names)
    return names


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


def check_item_exist(name: str):
    items = find_items_names()
    for item in items:
        if item == name:
            return True
    return False


def get_change(oldest, newest):
    if oldest == newest:
        return 100.0
    try:
        return ((newest - oldest) / oldest) * 100.0
    except ZeroDivisionError:
        return 0.0
