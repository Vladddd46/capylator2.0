import os
import json
from datetime import datetime


def is_file_exist(path):
    return os.path.exists(path)


# Define a custom JSON encoder for datedime
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            # Convert datetime object to ISO format string
            return obj.isoformat()
        return super().default(obj)


def save_json_data(path, data):
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4, cls=DateTimeEncoder)


def read_json_file(path):
    with open(path, "r") as json_file:
        json_data = json.load(json_file)
    return json_data
