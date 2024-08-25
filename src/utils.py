import os
import json


def is_file_exist(path):
    return os.path.exists(path)


def save_json_data(path, data):
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)


def read_json_file(path):
    with open(path, "r") as json_file:
        json_data = json.load(json_file)
    return json_data
