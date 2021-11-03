import os
import item


def find_items():
    items = []
    files = os.listdir('data/')
    for filename in files:
        items.append(item.Item(filename))
    print(items[0].get_path())
# TODO Add sorting of elements
    return items


def check_item_exist(name: str):
    items = find_items()
    for item in items:
        if item.get_uri() == name:
            return True
    return False
    

def get_names(items: item.Item):
    names = []
    for idx in range(len(items)):
        names.append(items[idx].get_name())
    return names
