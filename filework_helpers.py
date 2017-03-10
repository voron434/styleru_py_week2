import json
import os

def load_data(path):
    if not os.path.exists(path):
        return None
    with open(path, mode='r', encoding='utf-8') as my_file:
        data = json.load(my_file)
        return data

def dump_data(data, path):
    with open(path, mode='w', encoding='utf-8') as my_file:
        json.dump(data, my_file)