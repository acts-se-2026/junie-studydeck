import json
import os


def load(path):
    if not os.path.exists(path):
        return {"decks": [], "cards": []}
    with open(path) as f:
        return json.load(f)


def save(data, path):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
