
import json
from pathlib import Path


data_file = Path(__file__).parent / "students.json"


def load_records():
    if not data_file.exists():
        return {}

    try:
        with data_file.open("r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        return {}


def save_records(records):
    with data_file.open("w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)
