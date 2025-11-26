import json
import os

FILE_PATH = "gradebook.json"

def load_data():
    if not os.path.exists(FILE_PATH):
        return {"courses": []}
    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {"courses": []}

def save_data(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)
