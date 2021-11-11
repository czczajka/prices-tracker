import os
import item
import pandas as pd

from sql_app.database import SessionLocal, engine

# def find_items():
#     items = []
#     files = os.listdir('data/')
#     for filename in files:
#         items.append(item.Item(filename))
#     items.sort(key=lambda x: x.get_uri())
#     return items


def find_items():
    items = []
    df = pd.read_sql('SELECT * FROM item_entries', engine, index_col='id')
    products = set(df['item_name'])
    for prod in products:
        items.append(item.Item(prod))
    items.sort(key=lambda x: x.get_uri())
    return items


def check_item_exist(name: str):
    items = find_items()
    for x in items:
        if x.get_uri() == name:
            return True
    return False
    

def get_names(items: item.Item):
    names = []
    for idx in range(len(items)):
        names.append(items[idx].get_name())
    return names
