import os
import json
from datetime import datetime
from typing import Any, Dict
from src.entities.Language import Language


def is_file_exist(path: str) -> bool:
    """Check if a file exists at the given path."""
    return os.path.exists(path)


class CustomJSONEncoder(json.JSONEncoder):
    """Custom JSON encoder for datetime and Language objects."""

    def default(self, obj: Any) -> Any:
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, Language):
            return obj.value  # or obj.name if you prefer to serialize by name
        return super().default(obj)


def custom_decoder(dct: Dict[str, Any]) -> Dict[str, Any]:
    """Custom JSON decoder for datetime and Language objects."""
    for key, value in dct.items():
        if isinstance(value, str):
            # Handle datetime parsing
            try:
                dct[key] = datetime.fromisoformat(value)
            except ValueError:
                # Handle Language enum parsing
                if value in Language.__members__:
                    dct[key] = Language[value]
    return dct


def save_json_data(path: str, data: Any) -> None:
    """Save data to a JSON file, using custom encoder for datetime and Language objects."""
    try:
        with open(path, "w") as json_file:
            json.dump(data, json_file, indent=4, cls=CustomJSONEncoder)
    except IOError as e:
        print(f"Error writing to file {path}: {e}")


def read_json_file(path: str) -> Any:
    """Read data from a JSON file, using custom decoder for datetime and Language objects."""
    try:
        with open(path, "r") as json_file:
            return json.load(json_file, object_hook=custom_decoder)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error reading from file {path}: {e}")
        return None
